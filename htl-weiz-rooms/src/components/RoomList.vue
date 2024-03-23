<template>
  <div class="container">
    <h1 class="header">List of Rooms</h1>
    <table class="room-table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Description</th>
          <th>Occupied</th>
          <th>Action</th> <!-- New column for delete buttons -->
        </tr>
      </thead>
      <tbody>
        <tr v-for="room in rooms" :key="room.id">
          <td>{{ room.name }}</td>
          <td>{{ room.description }}</td>
          <td>{{ room.occupied ? 'Yes' : 'No' }}</td>
          <td><button @click="deleteRoom(room)">Delete</button></td> <!-- Delete button for each room -->
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

    const fetchRooms = async () => {
      try {
        const response = await axios.get('http://localhost:8000/rooms');
        rooms.value = response.data;
      } catch (error) {
        console.error('Error fetching rooms:', error);
      }
    };

    const deleteRoom = async (room) => {
      try {
        await axios.delete(`http://localhost:8000/rooms/${room.id}`);
        // Refresh the room list after deletion
        fetchRooms();
      } catch (error) {
        console.error('Error deleting room:', error);
      }
    };

    onMounted(fetchRooms);

    return {
      rooms,
      deleteRoom,
    };
  },
};
</script>

<style>
body {
  background-color: #2c2f33; /* Dark background */
  color: #fff; /* White text */
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Modern font */
}

.container {
  text-align: center;
}

.header {
  color: #7289da; /* Discord color template */
}

.room-table {
  width: 80%;
  margin: auto;
  border-collapse: collapse;
}

.room-table th, .room-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.room-table th {
  background-color: #7289da; /* Discord color template */
  color: #fff;
}
</style>
