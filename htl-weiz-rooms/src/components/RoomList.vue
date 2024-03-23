<template>
  <div>
    <h1>List of Rooms</h1>
    <ul>
      <li v-for="room in rooms" :key="room.id">{{ room.name }}</li>
    </ul>
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

    onMounted(fetchRooms);

    return {
      rooms,
    };
  },
};
</script>