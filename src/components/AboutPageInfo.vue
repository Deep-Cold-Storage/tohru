<template>
  <section>
    <h2>Hello,</h2>
    <h2>My name is<span class="text-green"> Tohru </span>!</h2>

    <img class="logo" src="../assets/tohru-logo.svg">

    <p>Web app created to help get between WSiZ university campuses using a private bus.</p>

    <button v-if="supportShareAPI" v-on:click="shareApp"><img class="button-icon" src="../assets/heart-icon.svg"/>SHARE</button>
  </section>
</template>

<script>
export default {
  name: "AboutPageInfo",

  data() {
    return {
      supportShareAPI: false,

      shareTitle: "Tohru - Bus App",
      shareURL: "https://tohru.sylvanas.dream/",
    }
  },

  methods: {
    // Shares link using Share API
    shareApp: function() {
      navigator.share({
        title: this.shareTitle,
        url: this.shareURL
      });
    },
  },

  mounted() {
    // Hides share button if not supported
    if (navigator.share) {
      this.supportShareAPI = true;
    };
  },
};
</script>

<style scoped>

h2 {
  line-height: 1;
}

button {
  color: #22A460;
  border: 2px solid #22A460;

  display: block;

  margin-top: 5vh;
  margin-bottom: 1vh;

  margin-left: auto;
  margin-right: auto;

  font-family: "Montserrat", sans-serif;
  font-size: 1.5rem;
  font-weight: 700;
  height: 4.0rem;

  background-color: Transparent;

  border-radius: 0.8rem;

  padding-left: 1.0rem;
  padding-right: 1.0rem;

  text-align: center;
  text-decoration: none;
  outline: none;
}

.logo {
  width: 30%;
  display: block;

  margin-left: auto;
  margin-right: auto;

  padding-top: 1.5vh;
  padding-bottom: 1.5vh;
}

.button-icon {
  display: inline;
  width: 1.5rem;
  vertical-align: middle;

  margin-right: 4px;
  margin-left: 4px;
}

.text-green {
  color: #22a460;
}

</style>
