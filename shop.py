import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

#Shop: отображение страницы товара
driver = webdriver.Chrome("C:\chromedriver")
driver.maximize_window()
time.sleep(5)
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
MyAccount = driver.find_element_by_link_text("My Account")
MyAccount.click()
username = driver.find_element_by_id("username")
username.send_keys("1@2.ru")
password = driver.find_element_by_id("password")
password.send_keys("Auto2022matioN")
wait = WebDriverWait(driver, 10)
login = driver.find_element_by_xpath("//input[@name='login']")
login.click()
Shop = driver.find_element_by_link_text("Shop")
Shop.click()
HTML5Forms = driver.find_element_by_xpath("//img[@title='Mastering HTML5 Forms']")
HTML5Forms.click()
Header = wait.until(
    EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "HTML5 Forms")
)

#Shop: количество товаров в категории
driver.execute_script("window.open();")
window_item_in_cat = driver.window_handles[1]
driver.switch_to.window(window_item_in_cat)
driver.get("http://practice.automationtesting.in/")
MyAccount = driver.find_element_by_link_text("My Account")
MyAccount.click()
Logout = driver.find_element_by_xpath("//li[@class='woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout']/a")
Logout.click()
username = driver.find_element_by_id("username")
username.send_keys("1@2.ru")
password = driver.find_element_by_id("password")
password.send_keys("Auto2022matioN")
wait = WebDriverWait(driver, 10)
login = driver.find_element_by_xpath("//input[@name='login']")
login.click()
Shop = driver.find_element_by_link_text("Shop")
Shop.click()
HTML = driver.find_element_by_link_text("HTML")
HTML.click()
count = driver.find_elements_by_xpath("//a[@rel='nofollow']")
if len(count) == 3:
    print("3")
else:
    print("Ошибка")

#Shop: сортировка товаров
driver.execute_script("window.open();")
window_item_sort = driver.window_handles[2]
driver.switch_to.window(window_item_sort)
driver.get("http://practice.automationtesting.in/")
MyAccount = driver.find_element_by_link_text("My Account")
MyAccount.click()
Logout = driver.find_element_by_xpath("//li[@class='woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout']/a")
Logout.click()
username = driver.find_element_by_id("username")
username.send_keys("1@2.ru")
password = driver.find_element_by_id("password")
password.send_keys("Auto2022matioN")
wait = WebDriverWait(driver, 10)
login = driver.find_element_by_xpath("//input[@name='login']")
login.click()
Shop = driver.find_element_by_link_text("Shop")
Shop.click()
sorted_ = driver.find_element_by_xpath("//select")
sorted_select = sorted_.get_attribute("value")
if sorted_select == "menu_order":
    print("Default sorting")
else:
    print("Ошибка")
select_max_min = Select(sorted_)
select_max_min.select_by_value("price-desc")
sorted_1 = driver.find_element_by_xpath("//select")
sorted_select_1 = sorted_1.get_attribute("value")
if sorted_select_1 == "price-desc":
    print("Sort by price: high to low")
else:
    print("Ошибка")

#Shop: отображение, скидка товара
driver.execute_script("window.open();")
window_item_sale = driver.window_handles[3]
driver.switch_to.window(window_item_sale)
driver.get("http://practice.automationtesting.in/")
MyAccount = driver.find_element_by_link_text("My Account")
MyAccount.click()
Logout = driver.find_element_by_xpath("//li[@class='woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout']/a")
Logout.click()
username = driver.find_element_by_id("username")
username.send_keys("1@2.ru")
password = driver.find_element_by_id("password")
password.send_keys("Auto2022matioN")
wait = WebDriverWait(driver, 10)
login = driver.find_element_by_xpath("//input[@name='login']")
login.click()
Shop = driver.find_element_by_link_text("Shop")
Shop.click()
android = driver.find_element_by_xpath("//img[@title='Android Quick Start Guide']")
android.click()
OldPrice = driver.find_element_by_xpath("//del/span")
OldPrice_get_text = OldPrice.text
assert "₹600.00" in OldPrice_get_text
NewPrice = driver.find_element_by_xpath("//ins/span")
NewPrice_get_text = NewPrice.text
assert "₹450.00" in NewPrice_get_text
Book = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//img[@title='Android Quick Start Guide']"))
)
Book.click()
fullResImage = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "pp_close"))
)
fullResImage.click()

#Shop: проверка цены в корзине
driver.execute_script("window.open();")
window_item_price = driver.window_handles[4]
driver.switch_to.window(window_item_price)
driver.get("http://practice.automationtesting.in/")
wait = WebDriverWait(driver, 10)
MyAccount = driver.find_element_by_link_text("My Account")
MyAccount.click()
Logout = driver.find_element_by_xpath("//li[@class='woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout']/a")
Logout.click()
Shop = driver.find_element_by_link_text("Shop")
Shop.click()
BookAddToBasket = driver.find_element_by_xpath("//a[@data-product_id='182']")
BookAddToBasket.click()
time.sleep(5)
CartItem = driver.find_element_by_class_name("cartcontents")
CartItem_get_text = CartItem.text
assert "1 Item" in CartItem_get_text
Price = wait.until(
    EC.text_to_be_present_in_element((By.XPATH, "//a/span[@class='amount']"), "₹180.00")
)
cart = driver.find_element_by_xpath("//a[@title='View your shopping cart']")
cart.click()
Subtotal = wait.until(
    EC.text_to_be_present_in_element((By.XPATH, "//td[@data-title='Subtotal']"), "₹180.00")
)
Total = wait.until(
    EC.text_to_be_present_in_element((By.XPATH, "//tr[@class='order-total']/td/strong"), "₹189.00")
)

#Shop: работа в корзине
driver.execute_script("window.open();")
window_cart = driver.window_handles[5]
driver.switch_to.window(window_cart)
driver.get("http://practice.automationtesting.in/")
wait = WebDriverWait(driver, 10)
Shop = driver.find_element_by_link_text("Shop")
Shop.click()
Book1AddToBasket = driver.find_element_by_xpath("//a[@data-product_id='182']")
Book1AddToBasket.click()
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(5)
Book2AddToBasket = driver.find_element_by_xpath("//a[@data-product_id='180']")
Book2AddToBasket.click()
cart = driver.find_element_by_xpath("//a[@title='View your shopping cart']")
cart.click()
Delete = driver.find_element_by_xpath("//td[@class='product-remove']/a[@class='remove']")
time.sleep(5)
Delete.click()
Undo = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='woocommerce-message']/a"))
)
Undo.click()
Quantity = driver.find_element_by_xpath("//div[@class='quantity']/input")
Quantity.clear()
Quantity.send_keys("3")
update_cart = driver.find_element_by_xpath("//td[@colspan='6']/input[@name='update_cart']")
update_cart.click()
Quantity_value = Quantity.get_attribute("value")
assert "3" in Quantity_value
time.sleep(5)
coupon = driver.find_element_by_xpath("//div[@class='coupon']/input[@name='apply_coupon']")
coupon.click()
Error = driver.find_element_by_class_name("woocommerce-error")
Error_get_text = Error.text
assert "Please enter a coupon code." in Error_get_text

#Shop: покупка товара
driver.execute_script("window.open();")
window_buy = driver.window_handles[6]
driver.switch_to.window(window_buy)
driver.get("http://practice.automationtesting.in/")
wait = WebDriverWait(driver, 10)
Shop = driver.find_element_by_link_text("Shop")
Shop.click()
driver.execute_script("window.scrollBy(0, 300);")
Book1AddToBasket = driver.find_element_by_xpath("//a[@data-product_id='182']")
Book1AddToBasket.click()
time.sleep(5)
cart = driver.find_element_by_xpath("//a[@title='View your shopping cart']")
cart.click()
Checkout = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='wc-proceed-to-checkout']/a"))
)
Checkout.click()
FirstName = wait.until(
    EC.visibility_of_element_located((By.ID, "billing_first_name"))
)
FirstName.send_keys("Anna")
LastName = wait.until(
    EC.visibility_of_element_located((By.ID, "billing_last_name"))
)
LastName.send_keys("Brown")
email = wait.until(
    EC.visibility_of_element_located((By.ID, "billing_email"))
)
email.send_keys("1@2.ru")
phone = wait.until(
    EC.visibility_of_element_located((By.ID, "billing_phone"))
)
phone.send_keys("1234567890")
Country = driver.find_element_by_id("s2id_billing_country")
Country.click()
Country1 =driver.find_element_by_xpath("//div[@class='select2-search']/input")
Country1.send_keys("Russia")
Country2 = driver.find_element_by_id("select2-results-1")
Country2.click()
Adress = driver.find_element_by_id("billing_address_1")
Adress.send_keys("1132 Woodwind Trail")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("48840")
city = driver.find_element_by_id("billing_city")
city.send_keys("Haslett")
state = driver.find_element_by_id("billing_state")
state.send_keys("Oren")
payment = driver.find_element_by_id("payment_method_cheque")
payment.click()
place_order = driver.find_element_by_id("place_order")
place_order.click()
ThankYou = wait.until(
    EC.text_to_be_present_in_element((By.XPATH, "//p[@class='woocommerce-thankyou-order-received']"), "Thank you. Your order has been received.")
)
CheckPayments = wait.until(
    EC.text_to_be_present_in_element((By.XPATH, "//tfoot"), 'Check Payments')
)

