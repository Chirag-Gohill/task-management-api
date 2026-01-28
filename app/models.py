from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# ================= USER TABLE =================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, nullable=False)  # specify length
    hashed_password = Column(String(255), nullable=False)        # specify length
    is_active = Column(Boolean, default=True)

    tasks = relationship("Task", back_populates="owner")


# ================= TASK TABLE =================
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)  # specify length
    description = Column(String(1024))           # optional, specify max length
    completed = Column(Boolean, default=False)

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="tasks")