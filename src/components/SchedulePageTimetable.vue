<template>
  <section>
    <p><img class="clock-icon" src="../assets/clock-icon.svg"/>Day {{daySchedule.date}}</p>
    <div class="timetable">
      <transition-group name="list">
        <div :key="item" class="timetable-item" v-for="(item, key) in daySchedule.schedule" v-bind:key="item.offset">
          <div><h1 class="green">{{item[0]}}</h1></div> <div><h1>---</h1> </div> <div><h1 class="red">{{item[1]}}</h1></div>
        </div>
      </transition-group>
    </div>
    <button class="navigation-button"  v-on:click="previousDay()">PREVIOUS</button>
    <button class="navigation-button" v-on:click="nextDay()">NEXT</button>
  </section>
</template>

<script>
export default {
  name: "SchedulePageTimetable",
  props: {
    route: Object,
  },
  data() {
    return {
      dayOffset : 0,
      daySchedule: {},
    }
  },
  methods: {
    getScheduleData: function() {
      this.$http
        .get(
          "https://tohru.sylvanas.dream/schedules/?origin=" +this.route.origin +"&destination=" + this.route.destination + "&offset=" + this.dayOffset)
        .then(response => {
          if (response.data.status == "success") {
            this.daySchedule = response.data.payload;
          } else {
            this.daySchedule = {};
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    previousDay: function() {
      if (this.dayOffset > 0) {
          this.daySchedule = {};
          this.dayOffset =   this.dayOffset - 1;
      };
    },
    nextDay: function() {
      if (this.dayOffset < 30) {
          this.daySchedule = {};
          this.dayOffset =   this.dayOffset + 1;
      };
    },
  },
    watch: {
      "route.origin": function() {
        this.getScheduleData();
      },
      "route.destination": function() {
        this.getScheduleData();
      },
      "dayOffset": function() {
        console.log("WFT")
        this.getScheduleData();
      },
  },
  mounted() {
    this.getScheduleData();
  }
};
</script>

<style scoped>
.clock-icon {
  width: 20px;
  height: auto;
  vertical-align: middle;
  margin-right: 10px;
  margin-left: 4px;
}

h1 {
  text-align: center;
  margin-top: 1px;
}

.timetable {
  height: 70vh;
  overflow-y: auto;
  scroll-snap-type: y mandatory;
}

.timetable-item {
  scroll-snap-align: start;
}

.timetable-item div{
  width: 33.3%;
  display: inline-block;
}

.navigation-button {
  font-family: "Montserrat", sans-serif;
  height: 40px;
  font-size: 15px;
  font-weight: 700;
  border-radius: 8px;
  margin-top: 20px;
  border: 2px solid #353535;
  background-color: Transparent;

  color: #22a460;
  border: 2px solid #22a460;
  padding-left: 20px;
  padding-right: 20px;
  margin-right: 20px;
}

.green {
  color: #22A460;
}

.red {
  color: #FC736A;
}

.list-enter-active {
  transition: all 1s ease;
}
.list-enter {
  opacity: 0;
}

@media screen and (min-width: 900px) and (orientation: landscape) {
  .timetable::-webkit-scrollbar {
      display: none;
  }
}
</style>
