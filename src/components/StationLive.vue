<template>
  <div>
    <section>
      <h2>Departure in <span class="green">25</span> min</h2>
      <h2>At <span class="green">12:35</span></h2>
      <h2>Arriving at <span class="red">13:00</span></h2>
    </section>
  </div>
</template>

<script>
export default {
  name: "StationLive",
};
</script>

<style scoped>
h2 {
  text-align: left;
}

span {
  font-size: 30px;
}

section {
  line-height: 1.5;
  width: 75%;
  height: 50%;
  margin: 0 auto;
  padding-top: 10vh;
}

.green {
  color: #22a460;
}

.red {
  color: #fc736a;
}
</style>
