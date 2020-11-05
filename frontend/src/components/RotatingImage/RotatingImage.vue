<template>
  <div>
    <v-img height=100 contain class="animate__animated animate__tada animate__infinite animate__slower" v-bind:src= "require('../../images/' + image + '.png')"></v-img>
  </div>
</template>

<script>
import 'animate.css';

export default {
  name: 'RotatingImage',
  props:{
    "image": String
  },
}

</script>