PROJECT_NAME=chatbot_rag

# Levanta en modo desarrollo con hot reload
dev:
	docker compose up --build --remove-orphans --force-recreate

# Levanta en segundo plano
up:
	docker compose up -d

# Logs de la app
logs:
	docker compose logs -f $(PROJECT_NAME)

# Entra al contenedor con shell
sh:
	docker compose exec $(PROJECT_NAME) sh

# Para contenedores
stop:
	docker compose stop

# Baja contenedores y limpia red y volúmenes
down:
	docker compose down --volumes --remove-orphans

# Reconstrucción total ignorando caché
rebuild:
	docker compose build --no-cache

# Limpia basura de docker (imágenes huérfanas, volúmenes sin uso, etc)
clean-all:
	docker compose down --volumes --remove-orphans
	docker system prune -a --volumes -f

# Verifica uso de espacio
df:
	docker system df

# Ver servicios corriendo
ps:
	docker compose ps
