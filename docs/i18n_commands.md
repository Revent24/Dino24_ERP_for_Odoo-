## 🌐 Команды для работы с переводами модуля dino_erp_stock

Команды для экспорта и импорта языковых файлов (русский и украинский).

```bash
# 1. Перейти в папку Odoo и активировать venv
cd ~/OdooApps/odoo19
source ~/OdooApps/odoo19-venv/bin/activate

# 2. Экспорт русского языка (ru.po)
cd ~/OdooApps/odoo19
source ~/OdooApps/odoo19-venv/bin/activate
python3 -m odoo --addons-path=addons,../odoo_projects/dino24_addons i18n export -d dino24_dev -l ru_RU -o /home/steve/OdooApps/odoo_projects/dino24_addons/dino_erp_stock/i18n/ru.po dino_erp_stock

# 3. Экспорт украинского языка (uk.po)
python3 -m odoo --addons-path=addons,../odoo_projects/dino24_addons i18n export -d dino24_dev -l uk_UA -o /home/steve/OdooApps/odoo_projects/dino24_addons/dino_erp_stock/i18n/uk.po dino_erp_stock

# 4. После редактирования переводов: импорт в базу данных (с перезаписью)
python3 -m odoo server -d dino24_dev -u dino_erp_stock --addons-path=addons,../odoo_projects/dino24_addons --db_user=steve --http-port=8070 --i18n-overwrite
```

### Порядок работы:
1. Экспортируй языковые файлы командами выше
2. Отредактируй `ru.po` и `uk.po` файлы (переведи все `msgstr ""` на соответствующий язык)
3. Импортируй переводы обратно в базу с флагом `--i18n-overwrite`
4. Перезапусти сервер и обнови страницу в браузере
