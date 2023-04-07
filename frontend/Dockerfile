# Base image
FROM node:alpine as build

#incrementar la memoria de node
ENV NODE_OPTIONS=--max_old_space_size=4096


# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy app files
COPY . .


# Build app
RUN npm run build

# New base image
FROM nginx:alpine

# Copy build output to nginx
COPY --from=build /app/build /usr/share/nginx/html

# Copy custom nginx configuration

# Expose port 80
EXPOSE 80

# Start nginx server
CMD ["nginx", "-g", "daemon off;"]
