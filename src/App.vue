<template>
  <div id="app">
    <div id="slider">

      <section id="AboutPage">
        <AboutPage></AboutPage>
      </section>

      <section id="StationPage">
        <StationPage v-bind:data="info"></StationPage>
      </section>

      <section id="SchedulePage">
        <SchedulePage></SchedulePage>
      </section>

    </div>
    <TabBar></TabBar>
  </div>
</template>

<script>
import AboutPage from './components/AboutPage.vue'
import StationPage from './components/StationPage.vue'
import SchedulePage from './components/SchedulePage.vue'
import TabBar from './components/TabBar.vue'

export default {
  name: "app",
  data () {
    return {
      info: null
    }
  },
  components: {
    AboutPage,
    StationPage,
    SchedulePage,
    TabBar
  },

  methods:{
     scrollToStationPage: function() {
       this.$scrollTo("#StationPage", 0, { container: "#slider", cancelable: false, force: true, y: false, x: true} );
     }
 },
 mounted(){
    this.scrollToStationPage();

    this.$http
      .get("https://tohru.sylvanas.dream/v1/origins/")
      .then(response => (this.info = response.data.payload))
 },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Montserrat&display=swap");

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  overflow: hidden;
	background-color: #131313;

  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.page {
  height: 100vh;
  padding: 20px;
}

#slider {
	scroll-snap-type: x mandatory;
	display: flex;
	overflow-x: scroll;
}

#slider section {
	border: 0;
	min-width: 100vw;
	height: 100vh;
  scroll-snap-stop: always;
	scroll-snap-align: center;
	position: relative;
}

@media screen and (min-width: 900px) and (orientation: landscape){
  #slider section {
  	min-width: 33.33vw;
  }
}

</style>
