"""
Minimal Report Module
"""
import json
import logging
import random
import time

import socketio
from flask import Flask, render_template, send_file, make_response

from suadente.database import engine
from suadente.pdf import Report

APP = Flask(__name__)
APP.config["DEBUG"] = True
SIO = socketio.Server()
SIOAPP = socketio.WSGIApp(SIO, APP)


@APP.route("/")
def home():
    """Home Page handler."""
    return render_template("home.html", app="suadente", page="reports")


@SIO.on("start")
def message(sid, data):
    """Socket message updater."""
    logging.info(["message", sid, data])
    raw_reports = engine.execute("select * from reports")
    reports = validate_reports(raw_reports)
    SIO.emit("update", reports)


def validate_reports(raw_reports):
    """Validate reports from DB."""
    reports = list()
    for report_id, raw_report in raw_reports:
        try:
            report = json.loads(raw_report)
            report["id"] = report_id
            reports.append(report)
            print(report)
        except json.JSONDecodeError as msg:
            logging.error(msg)
    return reports


@APP.route("/report/<report_id>/format/<file_format>")
def report(report_id, file_format):
    """Home Page handler."""
    raw_reports = engine.execute("select * from reports where id = %s", (report_id))
    reports = validate_reports(raw_reports)
    if file_format == "pdf":
        report = Report(reports[0])
        report.render()
        return send_file(
            "report_%s.pdf" % report.id,
            as_attachment=True,
            attachment_filename="report_%s.pdf" % report.id,
            mimetype="application/pdf",
        )
