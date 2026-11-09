// Practice file, fiction. The AI Operator Series, Book 5, chapter 5.
// The site's FAQ. The answers reach the page only when someone clicks "Learn more".
// Facts come from practice/shared/harbor-home-business-facts.txt; that file wins.
var FAQ = [
  ["Do you do move-out cleans?", "Yes! Empty homes only. Give us a call."],
  ["Do you bring supplies?", "We bring everything, and our products are fragrance-free unless you ask otherwise."],
  ["What if I need to cancel?", "No problem. Just give us 48 hours' notice to avoid a fee."]
];

document.getElementById("faq-toggle").addEventListener("click", function () {
  var box = document.getElementById("faq");
  if (box.innerHTML) { box.innerHTML = ""; return; }
  box.innerHTML = FAQ.map(function (qa) {
    return "<h3>" + qa[0] + "</h3><p>" + qa[1] + "</p>";
  }).join("");
});
