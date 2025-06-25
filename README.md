# **"Pinspire" – A Pinterest-like API with Django REST Framework (DRF)**  

## **1. Project Overview**  
**Project Name**: **Pinspire** – A Pinterest-like Image Sharing API  
**Objective**: Build a RESTful API where users can **upload, save, and discover images**, organize them into **collections (boards)**, and interact via **likes, comments, and wishlists**.  

### **Key Features**  
✅ **User Authentication** (JWT) – Signup, Login, Profile Management  
✅ **Image Upload & Discovery** – Upload, browse, and search images  
✅ **Boards (Collections)** – Save pins to custom boards (e.g., "Travel Ideas", "Recipes")  
✅ **Likes & Comments** – Engage with pins  
✅ **Wishlist** – Save favorite pins for later  
✅ **Follow System** – Follow users and see their pins  

---

## **2. Functional Requirements**  

### **2.1 User Management**  
- **Signup** (`username`, `email`, `password`)  
- **Login/Logout** (JWT tokens)  
- **Profile Management** (Update bio, profile picture)  

### **2.2 Pins (Images)**  
- **Upload Pin** (Image, title, description, tags)  
- **View Pin Feed** (Publicly visible, paginated)  
- **Search Pins** (By title, tags, or user)  
- **Delete/Edit Pin** (Only the uploader can modify)  

### **2.3 Boards (Collections)**  
- **Create Board** (Name, description, visibility: *public/private*)  
- **Add Pin to Board** (Drag-and-drop-like functionality via API)  
- **View Boards** (List of a user’s boards)  
- **Delete/Edit Board** (Only the owner can modify)  

### **2.4 Interactions (Likes, Comments, Wishlist)**  
- **Like/Unlike a Pin** (Prevent duplicate likes)  
- **Comment on Pins** (Authenticated users only)  
- **Wishlist** (Save pins to a "Saved for Later" list)  

### **2.5 Social Features**  
- **Follow/Unfollow Users**  
- **Feed of Followed Users’ Pins**  

---

## **3. Technical Specifications**  

### **3.1 Tech Stack**  
- **Backend**: Django + Django REST Framework (DRF)  
- **Authentication**: JWT (SimpleJWT) 
- **Database**: PostgreSQL (or SQLite for dev)  
- **Image Storage**: `django-storages` (AWS S3 or local `ImageField`)  
- **API Docs**: Swagger/OpenAPI (DRF Spectacular) [Optional]

### **3.2 API Endpoints**  

| **Endpoint** | **Method** | **Description** | **Permissions** |
|-------------|-----------|----------------|----------------|
| `/api/auth/register/` | POST | User signup | Public |
| `/api/auth/login/` | POST | JWT login | Public |
| `/api/auth/refresh/` | POST | Refresh JWT token | Public |
| `/api/users/<username>/` | GET | User profile | Public |
| `/api/users/me/` | GET, PUT | Current user profile | Authenticated |
| `/api/pins/` | GET | List all pins (feed) | Public |
| `/api/pins/` | POST | Upload new pin | Authenticated |
| `/api/pins/<id>/` | GET, PUT, DELETE | Pin details & actions | Owner-only for edits |
| `/api/pins/search/?q=<query>` | GET | Search pins | Public |
| `/api/boards/` | GET, POST | List or create boards | Authenticated |
| `/api/boards/<id>/` | GET, PUT, DELETE | Board details & actions | Owner-only |
| `/api/boards/<id>/pins/` | POST | Add pin to board | Authenticated |
| `/api/pins/<id>/like/` | POST | Like/unlike pin | Authenticated |
| `/api/pins/<id>/comments/` | GET, POST | List/add comments | Public/Authenticated |
| `/api/wishlist/` | GET | Get wishlist pins | Authenticated |
| `/api/wishlist/<pin_id>/` | POST, DELETE | Add/remove from wishlist | Authenticated |
| `/api/users/<username>/follow/` | POST | Follow/unfollow user | Authenticated |

---

## **4. Non-Functional Requirements**  
- **Security**: JWT, rate limiting (optional)  
- **Performance**: Pagination, optimized queries (`select_related`, `prefetch_related`)  
- **Image Handling**: Compression, CDN (optional)  
- **Scalability**: Docker + AWS/GCP deployment (optional)  

---

## **5. Future Enhancements (Optional)**  
- **Tagging System** (Categorize pins by topics)  
- **Notifications** (When someone likes/comments on your pin)  
- **AI Recommendations** (Suggest pins based on interests)  
- **Collaborative Boards** (Multiple users can add to a board)  

---
