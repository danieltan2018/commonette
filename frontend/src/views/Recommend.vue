<template>
  <v-sheet class="mx-auto" elevation="8">
    <span>
      <h2>YouTube Recommendations</h2>
    </span>
    <v-slide-group class="pa-4" active-class="success" show-arrows>
      <v-slide-item v-for="video in youtubeResults" :key="video.id">
        <v-container grid-list-md>
          <v-card class="mx-auto" max-width="300px">
            <v-img :src="video.snippet.thumbnails.medium.url" contain></v-img>
            <v-card-title v-text="video.snippet.title" class="h3"></v-card-title>
            <v-card-subtitle>
              {{video.snippet.channelTitle}}
            </v-card-subtitle>
          </v-card>
        </v-container>
      </v-slide-item>
    </v-slide-group>
  </v-sheet>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    youtubeParams: {
      category: 0,
    },
    youtubeResults: {},
  }),
  created() {
    this.initialise();
  },
  methods: {
    initialise() {
      // Insert api call to backend
      // Update dummy values
      this.youtubeParams.category = 28;
      this.renderYoutube();
    },
    renderYoutube() {
      axios
        .get(
          "https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&maxResults=10&regionCode=SG&videoCategoryId=" +
            this.youtubeParams.category +
            "&key=AIzaSyA7Y61l8cbCs3iBaovaUT9iv8eczTikK9k"
        )
        .then((response) => {
          this.youtubeResults = response.data.items;
        });
    },
  },
};
</script>