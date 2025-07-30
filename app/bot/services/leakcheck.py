import aiohttp


async def check_email_leakcheck(email):
    url = f"https://leakcheck.io/api/public?key=free&check={email}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=10) as response:
            data = await response.json()

            if not data.get("success", False):
                return "Email не найден."

            if data.get("found", 0) > 0:
                leaks = data.get("sources", [])

                leaks_list = []
                for leak in leaks[:3]:
                    name = leak.get('name', 'Неизвестный источник')
                    date = leak.get('date', 'дата неизвестна')
                    leaks_list.append(f"• {name} ({date})")

                return (
                        "<b>Результат проверки</b>\n"
                        f"Email: <code>{email}</code>\n"
                        "<b>Обнаружены утечки</b>\n\n"
                        f"<b>Найдено:</b> в {data['found']} источниках\n"
                        f"<b>Последние утечки:</b>\n" +
                        "\n".join(leaks_list) + "\n\n"
                        "<i>Рекомендуем сменить пароли на этих сервисах!</i>"
                )

            return (
                "<b>Результат проверки</b>\n"
                f"Email: <code>{email}</code>\n"
                "<b>Утечек не обнаружено</b>\n\n"
                "<i>Этот email не найден в известных базах утечек.</i>"
            )