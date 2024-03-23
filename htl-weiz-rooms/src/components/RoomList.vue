<template>
  <div class="container">
    

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

    const fetchRooms = async () => {
      try {
        const response = await axios.get('http://localhost:8000/rooms');
        rooms.value = response.data;
      } catch (error) {
        console.error('Error fetching rooms:', error);
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
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Modern font */
}

.header {
  color: #7289da; /* Discord color template */
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