import os
from flask import Flask, send_from_directory,jsonify

app = Flask(__name__, static_folder="dist", static_url_path="")



receipts = {
    "8DEB11A545EE76E": {
        "code": "8DEB11A545EE76E",
        "description": "BUSINESS PERMIT BILL FOR YEAR-2026, OWNER :",
        "document_date": "2026-06-16 18:10:02",
        "generated_by": "REHEMA OMAR",
        "amount": "1000000.00",
        "issued_to": "BUSINESS PERMIT BILL FOR YEAR-2026, OWNER :",
        "sub_county": "",
        "ward": "",
        "zone": ""
    },
    "XYZ123456789": {
        "code": "XYZ123456789",
        "description": "PHARMACY RECEIPT - SALE",
        "document_date": "2026-06-17 12:15:00",
        "generated_by": "LATE NIGHT CHEMIST",
        "amount": "1500.00",
        "issued_to": "Customer: John Doe",
        "sub_county": "Kwale",
        "ward": "Ward 5",
        "zone": "Zone A"
    },
    "8DE6D728FF73D97": {
        "code": "8DE6D728FF73D97",
        "description": "Sand & Stone Cess",
        "document_date": "2026-06-27 15:10:02",
        "generated_by": "MARIAM BAYA",
        "amount": "131400.00",
        "issued_to": "Sand & Stone Cess",
        "sub_county": "",
        "ward": "",
        "zone": ""
    },
    "8DF1281867B6B1F": {
            "code": "ADEXYKWPLVA",
            "description": "ADVERT CHARGE FOR CLIENT",
            "document_date": "2026-09-14 15:10:02",
            "generated_by": "CATHERINE MBULWA",
            "amount": "600000.00",
            "issued_to": "ADVERT CHARGE FOR CLIENT",
            "sub_county": "",
            "ward": "",
            "zone": ""
        },
}

@app.route("/api/validate/<code>")
def validate(code):
    receipt = receipts.get(code)
    if receipt:
        return jsonify(receipt)
    return jsonify({"error": "Receipt not found"}), 404

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    full_path = os.path.join(app.static_folder, path)
    if path and os.path.exists(full_path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

