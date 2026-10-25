PRICE = "$97 for the 90-day membership"   # <-- PRICE: change here, then run: python3 gen.py
EMAIL = "toby0562@mail.grokbot.com"
ADDRESS = "[Business mailing address to be added]"  # <-- MAILING ADDRESS placeholder
N = "CENTIN Publishing LLC"
CSS = """body{margin:0;font-family:system-ui,Arial,sans-serif;line-height:1.6;color:#1d2433;background:#fff}
.w{max-width:820px;margin:0 auto;padding:0 20px}header{background:#14213d;color:#fff;padding:14px 0}
header a{color:#fff;text-decoration:none;margin-right:14px}header b{font-size:1.15em;margin-right:24px}
.hero{background:#eef2f8;padding:40px 0}h1{font-size:1.9em;line-height:1.25}h2{color:#14213d;margin-top:34px}
.btn{display:inline-block;background:#fca311;color:#14213d;font-weight:700;padding:12px 22px;border-radius:6px;text-decoration:none}
.box{border:1px solid #d6dce8;border-radius:8px;padding:16px;margin:12px 0}.note{font-size:.9em;color:#555}
footer{background:#14213d;color:#cfd6e4;padding:24px 0;margin-top:40px;font-size:.9em}footer a{color:#fff;margin-right:14px}"""
WL = f"mailto:{EMAIL}?subject=Trust%20in%2090%20waitlist&body=Please%20notify%20me%20when%20Trust%20in%2090%20opens."
def page(fn, title, body):
    open(fn,"w").write(f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | {N}</title><meta name="description" content="{N} publishes Trust in 90, a digital 90-day membership for new managers."><style>{CSS}</style></head><body>
<header><div class="w"><b>{N}</b><a href="index.html">Home</a><a href="index.html#contact">Contact</a></div></header>
{body}
<footer><div class="w"><p><b>{N}</b> &middot; {EMAIL} &middot; {ADDRESS}</p>
<p><a href="index.html">Home</a><a href="refund.html">Refund Policy</a><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Service</a><a href="index.html#contact">Contact</a></p>
<p>Our products are training and self-help tools. They are not HR or legal advice.</p><p>&copy; 2026 {N}. All rights reserved.</p></div></footer></body></html>""")
page("index.html","Trust in 90 for New Managers",f"""
<section class="hero"><div class="w"><p><b>Launching soon from {N}</b></p>
<h1>Just promoted? Earn your team's trust in your first 90 days.</h1>
<p>Your first three months as a manager set the tone. Many new managers feel unsure how to lead people who were their peers, what their boss expects, or how to handle a hard talk. Trust in 90 gives you a clear week-by-week plan, so you know what to do next and your team sees a leader they can trust.</p>
<p><a class="btn" href="{WL}">Join the waitlist &ndash; get notified</a></p>
<p class="note">Trust in 90 is not open for purchase yet. Join the waitlist and we will email you when it opens.</p></div></section>
<div class="w">
<h2>What we do</h2><p>{N} creates and sells digital leadership training. Our first product is <b>Trust in 90</b>, an online membership for newly promoted managers.</p>
<h2>What you get</h2>
<div class="box"><b>The 90-Day Leadership Dashboard</b> (Google Sheet). A week-by-week plan built on five phases:
<ul><li><b>Listen</b> &ndash; weeks 1&ndash;2</li><li><b>Align</b> &ndash; weeks 3&ndash;4</li><li><b>Build Trust</b> &ndash; weeks 5&ndash;8</li><li><b>Create Early Wins</b> &ndash; weeks 9&ndash;11</li><li><b>Lead</b> &ndash; weeks 12&ndash;13</li></ul></div>
<div class="box"><b>Six kits that unlock as you need them</b>
<ul><li>Boss Alignment Kit &ndash; day 1</li><li>Listening Tour Kit &ndash; day 1</li><li>One-on-One Scripts &ndash; day 8</li><li>Hard Conversations Kit &ndash; day 29</li><li>Leading Through Change Kit &ndash; day 57</li><li>Weekly Rhythm Kit &ndash; day 78</li></ul>
We improve the kits based on member feedback, and we email members when a kit is updated.</div>
<h2>Price</h2><p class="box"><b>{PRICE}</b>. One-time payment. Backed by a 60-day money-back guarantee (<a href="refund.html">Refund Policy</a>).</p>
<h2>How it is delivered</h2><p>Everything is digital. After purchase, you get an email with your login to our online member area and a link to copy the Dashboard. Nothing is shipped.</p>
<h2>Who is behind it</h2><p>Trust in 90 was created by Paul Centinaro, founder of {N}. Paul is a retired Air Force lieutenant colonel who led a squadron of up to 250 people. He holds an MBA and is a Lean Six Sigma Black Belt. The plan is built on what he learned leading real teams.</p>
<h2 id="contact">Contact</h2><p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a><br>Mailing address: {ADDRESS}</p>
<p><a class="btn" href="{WL}">Join the waitlist &ndash; get notified</a></p></div>""")
page("refund.html","Refund Policy",f"""<div class="w"><h1>Refund Policy</h1>
<p>Trust in 90 comes with a <b>60-day money-back guarantee</b>. If you are not happy for any reason within 60 days of purchase, email <a href="mailto:{EMAIL}">{EMAIL}</a> with the email you used to buy. We will refund your full payment to your original payment method. No forms and no hard questions.</p>
<p>Refunds are usually processed within 5&ndash;10 business days. After a refund, access to the member area ends. Requests after 60 days are not eligible.</p></div>""")
page("privacy.html","Privacy Policy",f"""<div class="w"><h1>Privacy Policy</h1><p>Last updated: October 25, 2026</p>
<p><b>What we collect.</b> Your name and email when you join the waitlist or buy, and any messages you send us. Payments are handled by our payment processor. We do not see or store your full card number.</p>
<p><b>How we use it.</b> To deliver your membership, send product emails and kit updates, answer questions, and process refunds.</p>
<p><b>What we do not do.</b> We do not sell or rent your information. This website uses no tracking, ads, or analytics cookies.</p>
<p><b>Your choices.</b> You can unsubscribe from emails at any time, or ask us to see or delete your data by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<p><b>Service providers.</b> We use trusted providers for payments, email, and our member area. They only use your data to provide those services.</p></div>""")
page("terms.html","Terms of Service",f"""<div class="w"><h1>Terms of Service</h1><p>Last updated: October 25, 2026</p>
<p>These terms cover use of this website and the Trust in 90 membership sold by {N}.</p>
<p><b>The product.</b> Trust in 90 is a digital, 90-day online membership. It includes the 90-Day Leadership Dashboard and kits that unlock on a schedule. Nothing is shipped.</p>
<p><b>Your license.</b> You may use the materials for yourself and your own work. Please do not resell, share logins, or republish them.</p>
<p><b>Payment and refunds.</b> Prices are shown before you buy. Refunds follow our <a href="refund.html">Refund Policy</a>.</p>
<p><b>Not professional advice.</b> Our materials are training and self-help tools. They are not HR or legal advice. For HR or legal questions, talk to your HR team or a lawyer. Results depend on you; we do not promise any specific result.</p>
<p><b>Liability.</b> To the extent the law allows, our total liability is limited to the amount you paid us.</p>
<p><b>Changes.</b> We may update these terms and the product. Questions: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div>""")
