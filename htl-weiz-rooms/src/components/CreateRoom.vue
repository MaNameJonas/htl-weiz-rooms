<template>
  <div class="create-room">
    <h2>Create New Room</h2>
    <div class="input-group">
      <input type="text" id="name" v-model="newRoom.name" placeholder="Name" />
      <input type="text" id="description" v-model="newRoom.description" placeholder="Description" />
      <label for="occupied">Occupied:</label>
      <input type="checkbox" id="occupied" v-model="newRoom.occupied" />
      <button class="save-btn" @click="saveRoom">Save</button>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const newRoom = ref({ name: '', description: '', occupied: false });

    const saveRoom = async () => {
      try {
        await axios.post('http://localhost:8000/rooms', newRoom.value);
        // Clear the new room data
        newRoom.value = { name: '', description: '', occupied: false };
      } catch (error) {
        console.error('Error saving room:', error);
      }
    };

    return {
      newRoom,
      saveRoom,
    };
  },
};
</script>

<style scoped>
.input-group label {
  margin-right: 10px;
  width: 80px; 
  display: flex;
  align-items: center; 
}

.input-group {
  display: flex;
}

.input-group input[type="text"] {
  margin-right: 10px;
  width: 150px;
}

.input-group input[type="checkbox"] {
  margin-right: 10px;
}

.save-btn {
  background-color: #7289da;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.save-btn:hover {
  background-color: #5f73bc;
}

.create-room {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}
</style>
