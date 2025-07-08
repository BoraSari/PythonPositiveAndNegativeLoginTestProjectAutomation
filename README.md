Python Positive And Negative Login Test Project Automation
Project Overview
This project provides a comprehensive automated test suite for the login functionality of the N11 e-commerce website. It covers both positive (successful login) and negative (unsuccessful login with invalid credentials) scenarios to ensure the robustness and security of the authentication process. Developed using Python, Selenium WebDriver, and PyTest, it adheres to the Page Object Model (POM) for maintainability and uses python-dotenv for secure handling of sensitive login credentials.

Project Goal
The main objectives of this project are to:

Automate the login process to the N11 website.

Verify successful login with valid credentials.

Verify appropriate error messages and behavior for invalid login attempts.

Ensure the login functionality is secure and robust against common user input errors.

Showcase practical application of Python, Selenium WebDriver, and PyTest for comprehensive login test automation, including secure data handling.

Technologies Used
Programming Language: Python

Test Automation Framework: Selenium WebDriver

Testing Framework: PyTest

Browser Driver Management: WebDriverManager (for Chrome)

Design Pattern: Page Object Model (POM)

Environment Variables: python-dotenv (for managing sensitive data like username/password)

Setup and Run Instructions
To set up and run this project locally, follow these steps:

Clone the Repository:

git clone https://github.com/BoraSari/PythonPositiveAndNegativeLoginTestProjectAutomation.git
cd PythonPositiveAndNegativeLoginTestProjectAutomation

(Note: Replace BoraSari with your actual GitHub username if different. Adjust the repository name if it's different in your actual GitHub setup.)

Create and Activate Virtual Environment (Recommended):

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

Install Dependencies:

pip install -r requirements.txt

(You'll need a requirements.txt file in your project. You can generate it by running pip freeze > requirements.txt after installing all necessary libraries.)
(Common libraries to include: selenium, pytest, webdriver-manager, python-dotenv)

Configure Environment Variables:
Create a .env file in the root directory of the project and add your N11 login credentials for testing:

VALID_EMAIL="your_valid_email@example.com"
VALID_PASSWORD="your_valid_password"
INVALID_EMAIL="invalid_email@example.com"
INVALID_PASSWORD="invalid_password"

Make sure not to commit this .env file to your public repository! Add it to your .gitignore.

Run the Tests:

pytest -v

To run specific tests (e.g., positive or negative scenarios):

pytest -k "positive_login_test" -v
pytest -k "negative_login_test" -v

Test Coverage and Scenarios
This project covers the following key scenarios for N11's login functionality:

Positive Login Test:

Description: Verifies that a user can successfully log in to the N11 website using valid credentials.

Flow: Navigates to the N11 login page, enters a valid email and password (from .env), clicks the login button, and asserts that the user is successfully logged in (e.g., by checking for a profile element or a welcome message).

Negative Login Test (Invalid Credentials):

Description: Verifies that the website handles invalid login attempts correctly by displaying appropriate error messages.

Flow: Navigates to the N11 login page, enters invalid email and/or password (from .env), clicks the login button, and asserts that an expected error message is displayed (e.g., "Kullanıcı adı veya şifre hatalı" - Username or password incorrect).

Screenshots/GIFs
(Lütfen buraya test yürütmesini, başarılı giriş ekranını ve hatalı giriş denemelerindeki hata mesajlarını gösteren ekran görüntüleri veya GIF'ler ekleyerek projenin işlevselliğini görsel olarak sergileyin.)

License
This project is licensed under the MIT License - see the LICENSE file for details.

Python Pozitif ve Negatif Giriş Test Otomasyon Projesi
Projeye Genel Bakış
Bu proje, N11 e-ticaret web sitesinin giriş işlevselliği için kapsamlı bir otomatik test paketi sunar. Kimlik doğrulama sürecinin sağlamlığını ve güvenliğini sağlamak için hem pozitif (başarılı giriş) hem de negatif (geçersiz kimlik bilgileriyle başarısız giriş) senaryoları kapsar. Python, Selenium WebDriver ve PyTest kullanılarak geliştirilen bu proje, bakım kolaylığı için Page Object Model (POM) prensiplerine uyar ve hassas giriş kimlik bilgilerinin güvenli bir şekilde işlenmesi için python-dotenv kullanır.

Proje Amacı
Bu projenin temel hedefleri şunlardır:

N11 web sitesine giriş sürecini otomatikleştirmek.

Geçerli kimlik bilgileriyle başarılı girişi doğrulamak.

Geçersiz giriş denemeleri için uygun hata mesajlarını ve davranışını doğrulamak.

Giriş işlevselliğinin yaygın kullanıcı giriş hatalarına karşı güvenli ve sağlam olduğundan emin olmak.

Güvenli veri işleme dahil olmak üzere kapsamlı giriş testi otomasyonu için Python, Selenium WebDriver ve PyTest'in pratik uygulamasını sergilemek.

Kullanılan Teknolojiler
Programlama Dili: Python

Test Otomasyon Çerçevesi: Selenium WebDriver

Test Çerçevesi: PyTest

Tarayıcı Sürücüsü Yönetimi: WebDriverManager (Chrome için)

Tasarım Deseni: Page Object Model (POM)

Ortam Değişkenleri: python-dotenv (kullanıcı adı/parola gibi hassas verileri yönetmek için)

Kurulum ve Çalıştırma Talimatları
Bu projeyi yerel olarak kurmak ve çalıştırmak için aşağıdaki adımları izleyin:

Depoyu Klonlayın:

git clone https://github.com/BoraSari/PythonPositiveAndNegativeLoginTestProjectAutomation.git
cd PythonPositiveAndNegativeLoginTestProjectAutomation

(Not: BoraSari yerine gerçek GitHub kullanıcı adınızı yazın. GitHub'daki gerçek kurulumunuz farklıysa depo adını ayarlayın.)

Sanal Ortam Oluşturma ve Etkinleştirme (Önerilir):

python -m venv venv
# Windows'ta:
.\venv\Scripts\activate
# macOS/Linux'ta:
source venv/bin/activate

Bağımlılıkları Yükle:

pip install -r requirements.txt

(Projenizde bir requirements.txt dosyası bulunması gerekmektedir. Gerekli tüm kütüphaneleri kurduktan sonra pip freeze > requirements.txt komutuyla oluşturabilirsiniz.)
(Eklenecek yaygın kütüphaneler: selenium, pytest, webdriver-manager, python-dotenv)

Ortam Değişkenlerini Yapılandırın:
Projenin kök dizininde bir .env dosyası oluşturun ve test için N11 giriş kimlik bilgilerinizi ekleyin:

VALID_EMAIL="gecerli_eposta_adresiniz@ornek.com"
VALID_PASSWORD="gecerli_parolaniz"
INVALID_EMAIL="gecersiz_eposta@ornek.com"
INVALID_PASSWORD="gecersiz_parola"

Bu .env dosyasını herkese açık deponuza yüklememeye dikkat edin! .gitignore dosyanıza ekleyin.

Testleri Çalıştırın:

pytest -v

Belirli testleri çalıştırmak için (örn: pozitif veya negatif senaryolar):

pytest -k "positive_login_test" -v
pytest -k "negative_login_test" -v

Test Kapsamı ve Senaryoları
Bu proje, N11'in giriş işlevselliği için aşağıdaki temel senaryoları kapsar:

Pozitif Giriş Testi:

Açıklama: Bir kullanıcının geçerli kimlik bilgileriyle N11 web sitesine başarılı bir şekilde giriş yapabildiğini doğrular.

Akış: N11 giriş sayfasına gider, geçerli bir e-posta ve parola ( .env dosyasından) girer, giriş düğmesine tıklar ve kullanıcının başarılı bir şekilde giriş yaptığını doğrular (örn: bir profil öğesi veya hoş geldiniz mesajı kontrol edilerek).

Negatif Giriş Testi (Geçersiz Kimlik Bilgileri):

Açıklama: Web sitesinin geçersiz giriş denemelerini uygun hata mesajları görüntüleyerek doğru bir şekilde ele aldığını doğrular.

Akış: N11 giriş sayfasına gider, geçersiz e-posta ve/veya parola ( .env dosyasından) girer, giriş düğmesine tıklar ve beklenen bir hata mesajının görüntülendiğini doğrular (örn: "Kullanıcı adı veya şifre hatalı").

Ekran Görüntüleri/GIF'ler

Lisans
Bu proje MIT Lisansı altında lisanslanmıştır - daha fazla ayrıntı için LICENSE dosyasına bakın.
