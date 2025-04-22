<template>
  <div class="admin">
    <h1>Admin Dashboard</h1>
    <p>Here you can manage users and view system status.</p>
    <button class="btn">Manage Users</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return { data: {} };
  },
  async created() {
    const res = await axios.get('https://didactic-tribble-97j65vjp676wh975x-8000.app.github.dev/admin');
    this.data = res.data.admin;
  }
};
</script>
<style scoped>
.admin {
  text-align: center;
  padding: 50px;
}

.admin h1 {
  color: #333;
  font-size: 36px;
}

.admin p {
  font-size: 18px;
  margin-top: 20px;
}

.btn {
  background-color: #28a745;
  color: white;
  padding: 10px 20px;
  border: none;
  font-size: 18px;
  cursor: pointer;
  margin-top: 20px;
}

.btn:hover {
  background-color: #218838;
}
</style>