### Trello Support Bot

This is a Telegram bot designed to facilitate communication with the technical support department using Trello for issue tracking. The bot allows users to submit their technical issues or questions in a specific format, and it creates Trello cards for each submission. The Trello cards are organized into different lists based on the specified department or category.

#### Features:

- **Submission Format:** Users are instructed to submit their requests in a specific format, including a department code, name, and description of the problem.

- **Trello Integration:** The bot integrates with Trello to create cards dynamically based on the user's submission. Each card is placed in the corresponding Trello list according to the specified department.

- **Instruction and Guidelines:** The bot provides users with an instruction manual, guiding them on how to format their submissions correctly. This helps in maintaining consistency and clarity in issue reporting.

#### How to Use:

1. **Start Command:** Users initiate interaction with the bot using the `/start` command. This command forwards the user's message to a group chat for further processing.

2. **Instruction Button:** Users can access the instruction manual by clicking the "ℹ️Инструкция" (Instruction) button. This provides guidelines on how to format their technical support requests.

3. **Submission Processing:** Upon receiving a user's message, the bot forwards it to a group chat and acknowledges the submission. It then processes the message, extracts relevant information, and creates a Trello card.

4. **Trello Card Creation:** The bot dynamically determines the Trello list based on the department code provided by the user. It creates a card with the user's name, description of the problem, and a timestamp.

5. **Error Handling:** The bot includes error handling mechanisms to address issues that may arise during the submission or card creation process.

#### Technologies Used:

- **Python:** The bot is implemented in Python using the aiogram library for Telegram interaction.

- **Trello API:** Integration with Trello is achieved through the Trello API, allowing the bot to create cards dynamically.

- **dotenv:** Environment variables are managed using the dotenv library for enhanced security and configuration flexibility.

#### Instructions for Deployment:

1. Clone the repository to your local machine.
2. Set up a virtual environment and install the required dependencies from the `requirements.txt` file.
3. Create a `.env` file with the necessary Trello API key, token, Telegram bot API key, and other configuration parameters.
4. Run the bot script (`main.py`) to start the Telegram bot.

#### Contributors:

- Islambek Shamshiev


---

### Trello Support Bot (RU)

Этот бот для Telegram предназначен для упрощения взаимодействия с техническим отделом с использованием Trello для отслеживания проблем. Бот позволяет пользователям отправлять свои технические вопросы или проблемы в определенном формате, и создает карточки Trello для каждой заявки. Карточки Trello организованы в различные списки в зависимости от указанного отдела или категории.

#### Особенности:

- **Формат подачи:** Пользователям предлагается отправлять свои запросы в определенном формате, включая код отдела, имя и описание проблемы.

- **Интеграция с Trello:** Бот взаимодействует с Trello для динамического создания карточек на основе запросов пользователей. Каждая карточка размещается в соответствующем списке Trello в зависимости от указанного отдела.

- **Инструкция и рекомендации:** Бот предоставляет пользователям инструкцию, направляя их по процессу правильного форматирования и отправки запросов в техническую поддержку.

#### Как использовать:

1. **Команда /start:** Пользователи начинают взаимодействие с ботом, используя команду `/start`. Эта команда пересылает сообщение пользователя в групповой чат для дальнейшей обработки.

2. **Кнопка Инструкция:** Пользователи могут получить доступ к инструкции, нажав кнопку "ℹ️Инструкция". Это предоставляет рекомендации по форматированию запросов в техподдержку.

3. **Обработка запроса:** После получения сообщения пользователя, бот пересылает его в групповой чат и подтверждает получение. Затем он обрабатывает сообщение, извлекает необходимую информацию и создает карточку Trello.

4. **Создание карточки Trello:** Бот динамически определяет список Trello на основе кода отдела, предоставленного пользователем. Он создает карточку с именем пользователя, описанием проблемы и меткой времени.

5. **Обработка ошибок:** Бот включает механизмы обработки ошибок для решения проблем, которые могут возникнуть в процессе отправки или создания карточки.

#### Используемые технологии:

- **Python:** Бот реализован на Python с использованием библиотеки aiogram для взаимодействия с Telegram.

- **Trello API:** Интеграция с Trello осуществляется через Trello API, позволяя боту динамически создавать карточки.

- **dotenv:** Переменные окружения управляются с использованием библиотеки dotenv для повышения безопасности и гибкости конфигурации.

#### Инструкции по развертыванию:

1. Клонируйте репозиторий на свой локальный компьютер.
2. Создайте виртуальное окружение и установите необходимые зависимости из файла `requirements.txt`.
3. Создайте файл `.env` с необходимыми параметрами, такими как ключ API Trello, т

окен, ключ API бота Telegram и другие конфигурационные параметры.
4. Запустите скрипт бота (`main.py`), чтобы запустить бота Telegram.

#### Участники:
- Исламбек Шамшиев
