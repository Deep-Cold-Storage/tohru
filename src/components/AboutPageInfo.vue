<template>
  <section>
    <h2>Hello,</h2>
    <h2>My name is <span class="green">Tohru !</span></h2>
    <img src="../assets/tohru-logo.svg"></img>
    <p>Web app created to streamline getting between WSiZ university campuses using private bus.</p>
    <button v-on:click="share()"><img class="icon" src="../assets/heart-icon.svg">SHARE</button>
  </section>
</template>

<script>
export default {
  name: "AboutPageInfo",
  methods: {
    share: function() {
      if (navigator.share) {
        navigator.share({
          title: 'WebShare API Demo',
          url: 'https://tohru.sylvanas.dream'
        }).then(() => {
          console.log('Thanks for sharing!');
        })
        .catch(console.error);
      } else {
        console.log("Not supported!")
      }
    }
  }
};
</script>

<style scoped>
section {
  padding-top: 2vh;
  line-height: 1.5;
  width: 75%;
  margin: 0 auto;
}

.icon {
  display: inline;
  width: 14px;
  height: auto;
  vertical-align: middle;
  margin-right: 4px;
  margin-left: 2px;
  padding-top: 0;
  padding-bottom: 0;
}

img {
  width: 35%;
  display: block;
  margin-left: auto;
  margin-right: auto;
  padding-top: 2vh;
  padding-bottom: 2vh;
}

.green {
  color: #22a460;
}

button {
  font-family: "Montserrat", sans-serif;
  color: #22A460;
  height: 40px;
  padding-left: 10px;
  padding-right: 10px;
  margin-right: 10px;
  border-radius: 8px;
  font-weight: 700;
  font-size: 15px;
  text-align: center;
  text-decoration: none;
  border: 2px solid #22A460;
  outline: none;
  background-color: Transparent;
  display: block;
  margin-top: 5vh;
  margin-left: auto;
  margin-right: auto;
}
</style>
