<template>
  <div>
    <v-img id="img" v-bind:height="height" contain class="animate__animated animate__tada animate__infinite animate__slower" v-bind:src= "require('../../images/' + image + '.png')"></v-img>
  </div>
</template>

<script>
import 'animate.css';

export default {
  name: 'RotatingImage',
  props:{
    "image": String,
    "height": Number,
  },
}

</script>