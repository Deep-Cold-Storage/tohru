<template>
  <section>
    <h2>Hello,</h2>
    <h2>My name is <span class="color-green">Tohru</span> !</h2>

    <img class="tohru-logo" src="../assets/tohru-logo.svg"></img>

    <p>Web app created to streamline getting between WSiZ university campuses using private bus.</p>

    <button v-if="supportsShare" v-on:click="share()"><img class="icon" src="../assets/heart-icon.svg">SHARE</button>
  </section>
</template>

<script>
export default {
  name: "AboutPageInfo",
  data() {
    return {
      supportsShare: true
    }
  },

  methods: {
    share: function() {
      if (navigator.share) {
        navigator.share({
          title: "Tohru Dragon - The Bus App",
          url: "https://tohru.sylvanas.dream/"
        }).then(() => {
          console.log('Thanks for sharing!');
        })
        .catch(console.error);
      } else {
        console.log("Not supported!")
      }
    }
  },
  mounted() {
    if (navigator.share) {
      this.supportsShare = true;
    }
  }
};
</script>

<style scoped>

h2 {
  line-height: 1;
}

.tohru-logo {
  width: 30%;
  display: block;

  margin-left: auto;
  margin-right: auto;

  padding-top: 1.5vh;
  padding-bottom: 1.5vh;
}

.icon {
  display: inline;
  width: 1.5rem;
  vertical-align: middle;
  margin-right: 4px;
  margin-left: 4px;
}

.color-green {
  color: #22a460;
}

button {
  font-family: "Montserrat", sans-serif;
  font-size: 15px;
  font-weight: 700;

  text-align: center;
  text-decoration: none;

  color: #22A460;
  background-color: Transparent;

  padding: 8px; 

  border-radius: 8px;
  border: 2px solid #22A460;

  outline: none;
  display: block;
  margin-top: 5vh;
  margin-bottom: 1vh;
  margin-left: auto;
  margin-right: auto;
}
</style>
