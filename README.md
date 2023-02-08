
### Docker

### Команда для создания образов
```bash 
docker-compose build
```

### Команда для запуска контейнеров
```bash
docker-compose up -d
```

### Для создания superuser, в терминале выполните следующие команды. После этой команды переходите в консоль (/app #)
```bash
docker exec -it leaflet_project_web_1 sh
```

### После перехода в консоль(/app #), Создайте администратора командой

python manage.py createsuperuser

Для доступа в панель администратора перейдите по ссылке http://localhost:8008/admin




