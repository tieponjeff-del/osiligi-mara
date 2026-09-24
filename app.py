from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Iltolish Mara Schools - Where Education Meets Nature</title>
<script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-[#fff8ed]">

<header class="bg-green-900 text-white px-6 py-4 flex justify-between items-center">
  <h1 class="font-black text-xl">ILTOLISH MARA SCHOOLS</h1>
  <span class="bg-amber-400 text-black px-3 py-1 rounded-full text-xs font-bold">Day & Boarding | Mixed</span>
</header>

<div class="bg-gradient-to-br from-green-900 to-green-700 text-white text-center py-20 px-4">
  <h2 class="text-5xl font-black">ILTOLISH MARA SCHOOLS</h2>
  <p class="mt-4 text-amber-200 text-xl italic">"Where Education Meets Nature, Knowledge Finds Its Roots"</p>
  <p class="mt-2">P.O Box 322, Kilgoris - Trans Mara South | Overlooking Maasai Mara National Reserve</p>
  <div class="mt-8 flex justify-center gap-4">
    <a href="#admission" class="bg-amber-400 text-black px-8 py-3 rounded-full font-bold">Admission Open</a>
    <a href="#contact" class="border border-white px-8 py-3 rounded-full">Contact Us</a>
  </div>
</div>

<section class="max-w-6xl mx-auto grid md:grid-cols-4 gap-4 -mt-10 px-6">
  <div class="bg-white p-5 rounded-xl shadow text-center"><h3 class="font-bold">🔬 Science Lab</h3><p class="text-sm text-gray-600">Fully equipped</p></div>
  <div class="bg-white p-5 rounded-xl shadow text-center"><h3 class="font-bold">💻 Computer Lab</h3><p class="text-sm text-gray-600">Digital learning</p></div>
  <div class="bg-white p-5 rounded-xl shadow text-center"><h3 class="font-bold">🍽️ Dining Hall</h3><p class="text-sm text-gray-600">Multipurpose hall</p></div>
  <div class="bg-white p-5 rounded-xl shadow text-center"><h3 class="font-bold">🏫 CBE Curriculum</h3><p class="text-sm text-gray-600">Playgroup - Grade 9</p></div>
</section>

<section class="max-w-6xl mx-auto p-8 mt-10">
  <h2 class="text-3xl font-bold text-green-900">Academics</h2>
  <div class="grid md:grid-cols-3 gap-6 mt-6">
    <div class="bg-white border-l-4 border-green-700 p-4 rounded"><b>Early Years</b><br>Playgroup, PP1, PP2 - Foundation with nature</div>
    <div class="bg-white border-l-4 border-amber-400 p-4 rounded"><b>Primary School</b><br>Grade 1 - 6 | CBE Competency Based</div>
    <div class="bg-white border-l-4 border-green-700 p-4 rounded"><b>Junior School</b><br>Grade 7 - 9 | Boarding & Day</div>
  </div>
</section>

<section id="contact" class="bg-green-900 text-white p-8 text-center mt-10">
  <h2 class="text-2xl font-bold">Contact Us</h2>
  <p class="mt-3">Location: Trans Mara South, Kilgoris - Overlooking Maasai Mara</p>
  <p>Phone: 072X XXX XXX | Email: info@iltolishmaraschools.sc.ke</p>
  <p class="mt-4 text-amber-200">© 2026 Iltolish Mara Schools</p>
</section>

</body>
</html>
    """

if __name__ == '__main__':
    app.run(debug=True)
