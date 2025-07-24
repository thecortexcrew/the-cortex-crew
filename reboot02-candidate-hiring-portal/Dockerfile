# Use Node image to serve the static files
FROM node:20-alpine AS build

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Serve the build using a lightweight HTTP server
FROM nginx:alpine
COPY --from=build /app /usr/share/nginx/html
COPY --from=build /app/dist /usr/share/nginx/html

# Optional: configure Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf
ENV PORT 8080
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
