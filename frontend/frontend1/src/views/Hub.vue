<template>
  <div class="hub">
    <h1>Welcome to the Hub</h1>
    <p>This is the central dashboard. Here you'll see an overview of your activities.</p>
    <button class="btn">View More</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return { hub: "" };
  },
  async created() {
    const res = await axios.get('https://didactic-tribble-97j65vjp676wh975x-8000.app.github.dev//hub');
    this.hub = res.data.hub;
  }
};  
</script>
<style scoped>
.hub {
  text-align: center;
  padding: 50px;
}

.hub h1 {
  color: #333;
  font-size: 36px;
}

.hub p {
  font-size: 18px;
  margin-top: 20px;
}

.btn {
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  border: none;
  font-size: 18px;
  cursor: pointer;
  margin-top: 20px;
}

.btn:hover {
  background-color: #0056b3;
}
</style>