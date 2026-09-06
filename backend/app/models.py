import uuid
from datetime import datetime
from app import db

# Helper function to generate String IDs (matching your GraphQL String! id)
def generate_uuid():
    return str(uuid.uuid4())

class Profile(db.Model):
    __tablename__ = 'profiles'
    
    # Using String UUIDs to match your original GraphQL 'id: String!'
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    
    email = db.Column(db.String(120), unique=True, nullable=False)
    namaLengkap = db.Column(db.String(100), nullable=False)
    
    # REQUIRED FOR FLASK: Firebase hid passwords from you, but SQL needs them
    password_hash = db.Column(db.String(255), nullable=False)
    
    role = db.Column(db.String(20), default="admin", nullable=False)
    dibuatPada = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Establishes a relationship so you can easily access a user's reports 
    # e.g., user.pengaduans
    pengaduans = db.relationship('Pengaduan', backref='author', lazy=True)
    
    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "namaLengkap": self.namaLengkap,
            "role": self.role,
            "dibuatPada": self.dibuatPada.isoformat()
        }

class Pengaduan(db.Model):
    __tablename__ = 'pengaduans'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    
    # RELATIONAL UPGRADE: Replaces the duplicate email/namaLengkap strings
    profile_id = db.Column(db.String(36), db.ForeignKey('profiles.id'), nullable=False)
    
    description = db.Column(db.Text, nullable=False)
    lokasi = db.Column(db.String(255), nullable=False)
    
    # Nullable=True matches your GraphQL optional 'pictureUrl: String'
    pictureUrl = db.Column(db.String(255), nullable=True) 
    dibuatPada = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Added for the admin dashboard so they can track resolution
    status = db.Column(db.String(20), default="pending", nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "profile_id": self.profile_id,
            "author_name": self.author.namaLengkap, # Fetched via the relationship
            "description": self.description,
            "lokasi": self.lokasi,
            "pictureUrl": self.pictureUrl,
            "status": self.status,
            "dibuatPada": self.dibuatPada.isoformat()
        }