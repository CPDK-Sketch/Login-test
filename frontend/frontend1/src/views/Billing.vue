<template>
  <div class="billing">
    <h1>Billing Information</h1>
    <p>View your current and past invoices here.</p>
    <ul>
      <li>Invoice #1: Paid</li>
      <li>Invoice #2: Pending</li>
      <li>Invoice #3: Overdue</li>
    </ul>
    <button class="btn">View Payment Options</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return { billing: {} };
  },
  async created() {
    const res = await axios.get('https://didactic-tribble-97j65vjp676wh975x-8000.app.github.dev/billing');
    this.billing = res.data.billing;
  }
};
</script>
<style scoped>
.billing {
  text-align: center;
  padding: 50px;
}

.billing h1 {
  color: #333;
  font-size: 36px;
}

.billing p {
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
  background-color: #17a2b8;
  color: white;
  padding: 10px 20px;
  border: none;
  font-size: 18px;
  cursor: pointer;
  margin-top: 20px;
}

.btn:hover {
  background-color: #138496;
}
</style>