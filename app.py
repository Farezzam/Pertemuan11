from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        nama = request.form.get("nama")
        tanggal = request.form.get("tanggal")
        bulan = request.form.get("bulan")
        tahun = request.form.get("tahun")
        umur = request.form.get("umur")

        try:
            tahun = int(tahun)
            umur_dihitung = 2024 - tahun
            if int(umur) == umur_dihitung:
                result = f"Halo {nama}, umur Anda sudah benar dihitung berdasarkan tahun lahir!"
            else:
                result = f"Halo {nama}, umur Anda tidak sesuai dengan perhitungan tahun lahir."
        except ValueError:
            result = "Terjadi kesalahan input. Pastikan semua data diisi dengan benar."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
