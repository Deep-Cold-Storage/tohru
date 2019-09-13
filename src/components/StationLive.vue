<template>
  <div>
    <section>
      <h2>Departure in <span class="green">{{ betterPayload.until }}</span> min</h2>
      <h2>At <span class="green">{{ betterPayload.schedule[0][0] }}</span></h2>
      <h2>Arriving at <span class="red">{{ betterPayload.schedule[0][1] }}</span></h2>
      <h2 class="error" v-if="noDepartures"> No departures today!</h2>
    </section>
  </div>
</template>

<script>
export default {
  name: "StationLive",
  props: {
      payload: {}
  },
  data() {
    return {
      noDepartures: false
    }
  },
  computed: {
    betterPayload: function () {
      if (Object.keys(this.payload).length === 0){
        this.noDepartures = true;
        return {"until": "00", "schedule": [["00:00", "00:00"]]}
      }
      this.noDepartures = false;
      return this.payload
    }
  }
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

.error {
  padding-top: 10vh;
}

.green {
  color: #22a460;
}

.red {
  color: #fc736a;
}
</style>
