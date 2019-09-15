<template>
  <section>
    <h2>Hello,</h2>
    <h2>My name is<span class="green"> Tohru </span>!</h2>

    <img class="logo" src="../assets/tohru-logo.svg"></img>

    <p>Web app created to help get between WSiZ university campuses using the private bus.</p>

    <button class="button-share" v-if="supportShareAPI" v-on:click="shareApp"><img class="icon" src="../assets/heart-icon.svg">SHARE</button>
  </section>
</template>

<script>
export default {
  name: "AboutPageInfo",

  data() {
    return {
      supportShareAPI: true,

      shareTitle: "Tohru - Bus App",
      shareURL: "https://tohru.sylvanas.dream/",
    }
  },

  methods: {
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

.logo {
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

.green {
  color: #22a460;
}

.button-share {
  font-family: "Montserrat", sans-serif;
  font-size: 1.5rem;
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
