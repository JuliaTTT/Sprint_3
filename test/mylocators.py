username = "//form/fieldset[1]/div/div/input"  #Поле Имя в форме Регистрации
email_register = "//form/fieldset[2]/div/div/input" #Поле Email в форме Регистрации
email = "//form/fieldset[1]/div/div/input" #Поле Email в форме Входа
password = "//input[@type='password']" #Поле Password в формах Регистрации и Входа
register = "//button[text()='Зарегистрироваться']" #Кнопка Зарегистрироваться в форме Регистрации
enter = "//button[text()='Войти']" #Кнопка Войти в форме Входа
constructor = "//p[text()='Конструктор']" #Кнопка Конструктор в верхнем меню
burger_ingredients = "//section[contains(@class, 'BurgerIngredients')]" #Секция с ингридиентами бургера
personal_account = "//a[@href='/account']" #Кнопка Личный Кабинет
logo = "//a[@href='/']" #Кнопка логотипа
exit = "//button[text()='Выход']" #Кнопка Выход в Личном Кабинете
enter_account = "//button[text()='Войти в аккаунт']" #Кнопка Войти в Аккаунт на главной странице
fillings = "//div/span[text()='Начинки']" #Вкладка Начинки в Конструкторе
rolls = "//div/span[text()='Булки']" #Вкладка-кнопка Булки в Конструкторе
rolls_header = "//h2[text()='Булки']" #Объект вкладка для Булки
sauces = "//div/span[text()='Соусы']" #Вкладка-кнопка вкладка для Соусы
sauces_border = "//div/span[text()='Соусы']/parent::div" #Объект вкладка для Соусы
fillings_border = "//div/span[text()='Начинки']/parent::div" #Объект вкладка для Начинки
order = "//button[text()='Оформить заказ']" #Кнопка Оформить заказ
enter_from_registration = "//div/main/div/div/p/a[text()='Войти']" #Кнопка Войти в форме Регистрации
enter_from_restore_password = "//div/main/div/div/p/a[text()='Войти']" #Кнопка Войти в форме Восстановления Пароля
incorrect_password = "//p[text()='Некорректный пароль']" #Надпись "Некорректный пароль" в форме Регистрации
user_already_exists = "//p[text()='Такой пользователь уже существует']" #Надпись "Такой пользователь уже существует" в форме Регистрации