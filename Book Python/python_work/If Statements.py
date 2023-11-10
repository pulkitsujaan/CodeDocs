browsers=["chrome","safari","edge","brave"]

# for browser in browsers:
#     if browser=="crome":
#         browser="Chrome"
#     print(browser.title())

# for browser in browsers:
#     if browser!="crome":
#         print(browser.title())
#     else:
#         browser="Chrome"
#         print(browser.title())

if "chrome" in browsers:
    print("You are eligible")
if "google" not in browsers:
    print("You are not eligible")