import io
from datetime import date
from fastapi import APIRouter, Depends, Query
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.core.deps import get_db, require_roles
from app.services.esg import calculate_esg_snapshot


router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/esg", dependencies=[Depends(require_roles("admin", "manager", "auditor"))])
def esg_report(
    period_start: date = Query(...),
    period_end: date = Query(...),
    format: str = Query("csv"),
    db: Session = Depends(get_db),
):
    metrics = calculate_esg_snapshot(db, period_start, period_end)
    if format.lower() == "pdf":
        return _generate_pdf(metrics, period_start, period_end)
    return _generate_csv(metrics, period_start, period_end)


def _generate_csv(metrics: dict[str, float], period_start: date, period_end: date):
    output = io.StringIO()
    output.write("metric,value\n")
    output.write(f"period_start,{period_start}\n")
    output.write(f"period_end,{period_end}\n")
    for key, value in metrics.items():
        output.write(f"{key},{value}\n")
    output.seek(0)
    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=esg-report.csv"},
    )


def _generate_pdf(metrics: dict[str, float], period_start: date, period_end: date):
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, 760, "ESG & Net Zero Report")
    c.setFont("Helvetica", 10)
    c.drawString(40, 740, f"Period: {period_start} to {period_end}")

    y = 710
    for key, value in metrics.items():
        c.drawString(40, y, f"{key.replace('_', ' ').title()}: {value}")
        y -= 18
    c.showPage()
    c.save()

    buffer.seek(0)
    return StreamingResponse(
        buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=esg-report.pdf"},
    )
