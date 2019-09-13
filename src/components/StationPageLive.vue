<template>
  <section>
    <template v-if="!noDepartures">
      <h2>Departure in <span class="color-green">{{ livePayload.until }}</span> min</h2>
      <h2>At <span class="color-green">{{ livePayload.schedule[0][0] }}</span></h2>
      <h2>Arriving at <span class="color-red">{{ livePayload.schedule[0][1] }}</span></h2>
    </template>

    <template v-if="noDepartures">
      <h2 class="color-red">No departures!</h2>
      <p>Tohru couldn't find any close departures for today!</p>
      <p>You could always try to change selected route.</p>
    </template>
  </section>
</template>

<script>
export default {
  name: "StationPageLive",
  props: {
    route: Object
  },

  data() {
    return {
      noDepartures: false,
      intervalTimer: Object,
      livePayload: {"until": "00", "schedule": [["00:00", "00:00"]]}
    };
  },

  methods: {
    getLiveData: function() {
      this.$http
        .get("https://tohru.sylvanas.dream/live/?origin=" + this.route.origin + "&destination=" + this.route.destination)
        .then(response => {
          if (response.data.status == "success") {
            this.livePayload = response.data.payload;
            this.noDepartures = false;
          } else {
            this.livePayload = {};
            this.noDepartures = true;
          }
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  created() {
    this.getLiveData();

    var self = this;
    this.intervalTimer = setInterval(function() {
      self.getLiveData();
    }, 3600);
  }
};
</script>

<style scoped>
span {
  font-size: 3.0rem;
}

section {
  padding-top: 10vh;
}

.color-green {
  color: #22a460;
}

.color-red {
  color: #fc736a;
}
</style>
