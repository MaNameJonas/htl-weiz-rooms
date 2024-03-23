<template>
  <div class="container">
    <h1 class="header">List of Rooms</h1>

    <!-- Create Room Form -->
    <div class="create-room">
      <h2>Create New Room</h2>
      <div class="input-group">
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="newRoom.name" />
      </div>
      <div class="input-group">
        <label for="description">Description:</label>
        <input type="text" id="description" v-model="newRoom.description" />
      </div>
      <div class="input-group">
        <label for="occupied">Occupied:</label>
        <input type="checkbox" id="occupied" v-model="newRoom.occupied" />
      </div>
      <button class="save-btn" @click="saveRoom">Save</button>
    </div>

    <!-- Room List -->
    <table class="room-table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Description</th>
          <th>Occupied</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="room in rooms" :key="room.id">
          <td>{{ room.name }}</td>
          <td>{{ room.description }}</td>
          <td>{{ room.occupied ? 'Yes' : 'No' }}</td>
          <td>
            <button class="delete-btn" @click="deleteRoom(room.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const rooms = ref([]);
    const newRoom = ref({ name: '', description: '', occupied: false });

    const fetchRooms = async () => {
      try {
        const response = await axios.get('http://localhost:8000/rooms');
        rooms.value = response.data;
      } catch (error) {
        console.error('Error fetching rooms:', error);
      }
    };

    const saveRoom = async () => {
      try {
        await axios.post('http://localhost:8000/rooms', newRoom.value);
        // Clear the new room data
        newRoom.value = { name: '', description: '', occupied: false };
        // Fetch updated room list
        await fetchRooms();
      } catch (error) {
        console.error('Error saving room:', error);
      }
    };

    const deleteRoom = async (roomId) => {
      try {
        await axios.delete(`http://localhost:8000/rooms/${roomId}`);
        // Fetch updated room list
        await fetchRooms();
      } catch (error) {
        console.error('Error deleting room:', error);
      }
    };

    onMounted(fetchRooms);

    return {
      rooms,
      newRoom,
      saveRoom,
      deleteRoom,
    };
  },
};
</script>

<style>
.container {
  text-align: center;
  background-color: #2c2f33; /* Dark background */
  color: #fff; /* White text */
}

.header {
  color: #7289da; /* Discord color template */
}

.create-room {
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.input-group {
  margin-bottom: 10px;
  display: flex;
  align-items: center;
}

.input-group label {
  display: inline-block;
  width: 100px;
  text-align: right;
  margin-right: 10px;
}

.input-group input[type="text"],
.input-group input[type="checkbox"] {
  width: 200px;
}

.save-btn {
  background-color: #7289da; /* Discord color template */
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.save-btn:hover {
  background-color: #5f73bc; /* Darker shade of Discord color */
}

.delete-btn {
  background-color: #ff0000; /* Red color for delete button */
  color: #fff;
  border: none;
  padding: 5px 10px;
  border-radius: 3px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.delete-btn:hover {
  background-color: #cc0000; /* Darker shade of red */
}

.room-table {
  width: 80%;
  margin: auto;
  border-collapse: collapse;
}

.room-table th,
.room-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.room-table th {
  background-color: #7289da; /* Discord color template */
  color: #fff;
}
</style>
