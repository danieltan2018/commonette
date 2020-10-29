<template>
  <v-main class="home">
    <div class="row">
      <div class="col-1"></div>
      <div class="col-5" data-aos="fade-down-right" data-aos-duration="1000" v-if="youtubeReady">
        <v-card type="chart" dark>
          <v-card-title>
            <v-icon color="red" large>mdi-youtube</v-icon>
            Youtube
          </v-card-title>
          <div class="chart-area">
            <bar-chart style="height: 100%" chart-id="youtubeStats" :chart-data="youtubeBarChart.chartData" :gradient-stops="youtubeBarChart.gradientStops" :extra-options="youtubeBarChart.extraOptions">
            </bar-chart>
          </div>
        </v-card>
      </div>
      <div class="col-5" data-aos="fade-down-left" data-aos-duration="1000" data-aos-delay="500" v-if="bookReady">
        <v-card type="chart" dark>
          <v-card-title>
            <v-icon color="blue" large>mdi-book</v-icon>Book
          </v-card-title>
          <div class="chart-area">
            <bar-chart style="height: 100%" chart-id="bookStats" :chart-data="bookBarChart.chartData" :gradient-stops="bookBarChart.gradientStops" :extra-options="bookBarChart.extraOptions">
            </bar-chart>
          </div>
        </v-card>
      </div>
      <div class="col-1"></div>
    </div>
    <div class="row">
      <div class="col-1"></div>
      <div class="col-5" data-aos="fade-up-right" data-aos-duration="1000" data-aos-delay="1000" v-if="movieReady">
        <v-card type="chart" dark>
          <v-card-title>
            <v-icon color="rgb(255, 0, 128)" large>mdi-movie-open</v-icon>Movie
          </v-card-title>
          <div class="chart-area">
            <bar-chart style="height: 100%" chart-id="movieStats" :chart-data="movieBarChart.chartData" :gradient-stops="movieBarChart.gradientStops" :extra-options="movieBarChart.extraOptions">
            </bar-chart>
          </div>
        </v-card>
      </div>
      <div class="col-5" data-aos="fade-up-left" data-aos-duration="1000" data-aos-delay="1500" v-if="spotifyReady">
        <v-card type="chart" dark>
          <v-card-title>
            <v-icon color="green" large>mdi-spotify</v-icon>Spotify
          </v-card-title>
          <div class="chart-area">
            <bar-chart style="height: 100%" chart-id="spotifyStats" :chart-data="spotifyBarChart.chartData" :gradient-stops="spotifyBarChart.gradientStops" :extra-options="spotifyBarChart.extraOptions">
            </bar-chart>
          </div>
        </v-card>
      </div>
      <div class="col-1"></div>
    </div>
  </v-main>
</template>

<script>
import BarChart from "../components/Charts/BarChart";
import * as chartConfigs from "../components/Charts/config";
import config from "../config";
import axios from "axios";
export default {
  components: {
    BarChart,
  },
  props: {
    roomCode: {
      type: String,
      default: "",
    },
  },
  data: () => ({
    roomUsers: [],
    userCount: 0,
    youtubeReady: false,
    bookReady: false,
    movieReady: false,
    spotifyReady: false,
    youtubeBarChart: {
      extraOptions: chartConfigs.barChartOptions,
      chartData: {
        labels: [],
        datasets: [
          {
            label: "Weight",
            fill: true,
            borderColor: "red",
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            data: [],
          },
        ],
      },
      gradientColors: config.colors.primaryGradient,
      gradientStops: [1, 0.4, 0],
    },
    bookBarChart: {
      extraOptions: chartConfigs.barChartOptions,
      chartData: {
        labels: [],
        datasets: [
          {
            label: "Weight",
            fill: true,
            borderColor: config.colors.info,
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            data: [],
          },
        ],
      },
      gradientColors: config.colors.primaryGradient,
      gradientStops: [1, 0.4, 0],
    },
    movieBarChart: {
      extraOptions: chartConfigs.barChartOptions,
      chartData: {
        labels: [],
        datasets: [
          {
            label: "Weight",
            fill: true,
            borderColor: "rgb(255, 0, 128)",
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            data: [],
          },
        ],
      },
      gradientColors: config.colors.primaryGradient,
      gradientStops: [1, 0.4, 0],
    },
    spotifyBarChart: {
      extraOptions: chartConfigs.barChartOptions,
      chartData: {
        labels: [],
        datasets: [
          {
            label: "Weight",
            fill: true,
            borderColor: "green",
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            data: [],
          },
        ],
      },
      gradientColors: config.colors.primaryGradient,
      gradientStops: [1, 0.4, 0],
    },
  }),
  created() {
    this.initialise();
  },
  mounted: function () {
    window.scrollTo(0, 0);
  },
  methods: {
    navigateRoute(newpath) {
      this.$router.push(newpath);
    },
    initialise() {
      axios({
        url: "/room/" + this.roomCode,
        method: "GET",
      })
        .then((response) => {
          localStorage.clear();
          localStorage.setItem("roomName", response.data.room_name);
          localStorage.setItem("roomCode", this.roomCode);
          if (response.data.questionnaire) {
            for (var person of response.data.questionnaire) {
              this.roomUsers.push({
                name: person.name,
                gender: person.gender,
              });
            }
            localStorage.setItem("roomUsers", JSON.stringify(this.roomUsers));
            this.userCount = this.roomUsers.length;
          } else {
            this.$bus.$emit("updated", "joined");
            this.navigateRoute("/questionnaire");
          }
          this.$bus.$emit("updated", "joined");
        })
        .catch(() => {
          this.navigateRoute("/");
        });
      axios.get("/dashboard/" + this.roomCode).then((response) => {
        for (const [key, value] of Object.entries(response.data.youtube)) {
          this.youtubeBarChart.chartData.labels.push(key);
          this.youtubeBarChart.chartData.datasets[0].data.push(value);
        }
        this.youtubeReady = true;
        for (const [key, value] of Object.entries(response.data.book)) {
          this.bookBarChart.chartData.labels.push(key);
          this.bookBarChart.chartData.datasets[0].data.push(value);
        }
        this.bookReady = true;
        for (const [key, value] of Object.entries(response.data.movie)) {
          this.movieBarChart.chartData.labels.push(key);
          this.movieBarChart.chartData.datasets[0].data.push(value);
        }
        this.movieReady = true;
        for (const [key, value] of Object.entries(response.data.spotify)) {
          this.spotifyBarChart.chartData.labels.push(key);
          this.spotifyBarChart.chartData.datasets[0].data.push(value);
        }
        this.spotifyReady = true;
      });
    },
  },
};
</script>
<style>
.home {
  background-color: rgb(81, 81, 118);
  justify-content: center;
}
</style>