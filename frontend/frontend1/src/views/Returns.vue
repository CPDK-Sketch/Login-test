<template>
  <div class="returns">
    <h1>Your Returns</h1>
    <p>Here are your past returns and their statuses.</p>
    <ul>
      <li>Return #1: Status - Pending</li>
      <li>Return #2: Status - Approved</li>
      <li>Return #3: Status - Processed</li>
    </ul>
    <button class="btn">Request New Return</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return { returns: [] };
  },
  async created() {
    const res = await axios.get('https://didactic-tribble-97j65vjp676wh975x-8000.app.github.dev/returns');
    this.returns = res.data.returns;
  }
};
</script>



<style scoped>
.returns {
  text-align: center;
  padding: 50px;
}

.returns h1 {
  color: #333;
  font-size: 36px;
}

.returns p {
  font-size: 18px;
  margin-top: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  font-size: 16px;
  margin-top: 10px;
}

.btn {
  background-color: #ff5722;
  color: white;
  padding: 10px 20px;
  border: none;
  font-size: 18px;
  cursor: pointer;
  margin-top: 20px;
}

.btn:hover {
  background-color: #e64a19;
}
</style>