<template>
  <div id="app">
    <h1 class="header">HTL Weiz Räume</h1>
    <CreateRoom />
    <RoomList />
  </div>
</template>

<script>
import RoomList from './components/RoomList.vue';
import CreateRoom from './components/CreateRoom.vue';

export default {
  name: 'App',
  components: {
    RoomList,
    CreateRoom,
  },
};
</script>

<style>
h1 {
  text-align: center;
  font-size: 50px;
}


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