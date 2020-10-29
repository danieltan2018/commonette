<template>
  <v-main class="home">
    youtube: {{youtubeTop}}<br>
    movie: {{movieTop}}<br>
    spotify: {{spotifyTop}}<br>
    book:{{ bookTop }}<br>
    users: {{roomUsers}}
    <!-- <div class="row">
      <div class="col-lg-4" >
        <v-card type="chart" dark>
          <div class="chart-area">
            <line-chart style="height: 100%" chart-id="purple-line-chart" :chart-data="purpleLineChart.chartData" :gradient-colors="purpleLineChart.gradientColors" :gradient-stops="purpleLineChart.gradientStops" :extra-options="purpleLineChart.extraOptions">
            </line-chart>
          </div>
        </v-card>
      </div>
    </div> -->
    <div class="row">
      <div class="col-1"></div>
      <div class="col-4">
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
      <div class="col-1"></div>
      <div class="col-5"></div>
      <div class="col-1"></div>
    </div>
    <div class="row">
      <div class="col-1"></div>
      <div class="col-5"></div>
      <div class="col-1"></div>
      <div class="col-4">
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
      <div class="col-1"></div>
    </div>
    <div class="row">
      <div class="col-1"></div>
      <div class="col-4">
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
      <div class="col-5"></div>
      <div class="col-1"></div>
    </div>
    <div class="row">
      <div class="col-1"></div>
      <div class="col-5"></div>
      <div class="col-1"></div>
      <div class="col-4">
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
    <!-- <div class="row">
      <div class="col-lg-4">
        <v-card type="chart" dark>
          <div class="chart-area">
            <line-chart style="height: 100%" chart-id="green-line-chart" :chart-data="greenLineChart.chartData" :gradient-stops="greenLineChart.gradientStops" :extra-options="greenLineChart.extraOptions">
            </line-chart>
          </div>
        </v-card>
      </div>
    </div> -->
  </v-main>
</template>

<script>
// import LineChart from '../components/Charts/LineChart';
import BarChart from "../components/Charts/BarChart";
import * as chartConfigs from "../components/Charts/config";
import config from "../config";
import axios from "axios";
export default {
  components: {
    // LineChart,
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
    youtubeTop: [],
    bookTop: [],
    movieTop: [],
    spotifyTop: [],
    // purpleLineChart: {
    //   extraOptions: chartConfigs.purpleChartOptions,
    //   chartData: {
    //     labels: ['JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
    //     datasets: [{
    //       label: "Data",
    //       fill: true,
    //       borderColor: config.colors.primary,
    //       borderWidth: 2,
    //       borderDash: [],
    //       borderDashOffset: 0.0,
    //       pointBackgroundColor: config.colors.primary,
    //       pointBorderColor: 'rgba(255,255,255,0)',
    //       pointHoverBackgroundColor: config.colors.primary,
    //       pointBorderWidth: 20,
    //       pointHoverRadius: 4,
    //       pointHoverBorderWidth: 15,
    //       pointRadius: 4,
    //       data: [80, 100, 70, 80, 120, 80],
    //     }]
    //   },
    //   gradientColors: config.colors.primaryGradient,
    //   gradientStops: [1, 0.2, 0],
    // },
    // greenLineChart: {
    //   extraOptions: chartConfigs.greenChartOptions,
    //   chartData: {
    //     labels: ['JUL', 'AUG', 'SEP', 'OCT', 'NOV'],
    //     datasets: [{
    //       label: "My First dataset",
    //       fill: true,
    //       borderColor: config.colors.danger,
    //       borderWidth: 2,
    //       borderDash: [],
    //       borderDashOffset: 0.0,
    //       pointBackgroundColor: config.colors.danger,
    //       pointBorderColor: 'rgba(255,255,255,0)',
    //       pointHoverBackgroundColor: config.colors.danger,
    //       pointBorderWidth: 20,
    //       pointHoverRadius: 4,
    //       pointHoverBorderWidth: 15,
    //       pointRadius: 4,
    //       data: [90, 27, 60, 12, 80],
    //     }]
    //   },
    //   gradientColors: ['rgba(66,134,121,0.15)', 'rgba(66,134,121,0.0)', 'rgba(66,134,121,0)'],
    //   gradientStops: [1, 0.4, 0],
    // },
    bookBarChart: {
      extraOptions: chartConfigs.barChartOptions,
      chartData: {
        labels: ["Business"],
        datasets: [
          {
            label: "No. of Users",
            fill: true,
            borderColor: config.colors.info,
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            data: [15],
          },
        ],
      },
      gradientColors: config.colors.primaryGradient,
      gradientStops: [1, 0.4, 0],
    },
    youtubeBarChart: {
      extraOptions: chartConfigs.barChartOptions,
      chartData: {
        labels: ["Film & Animation", "Entertainment"],
        datasets: [
          {
            label: "No. of Users",
            fill: true,
            borderColor: "red",
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            data: [9, 8],
          },
        ],
      },
      gradientColors: config.colors.primaryGradient,
      gradientStops: [1, 0.4, 0],
    },
    spotifyBarChart: {
      extraOptions: chartConfigs.barChartOptions,
      chartData: {
        labels: ["k-pop", "pop"],
        datasets: [
          {
            label: "No. of Users",
            fill: true,
            borderColor: "green",
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            data: [12, 8],
          },
        ],
      },
      gradientColors: config.colors.primaryGradient,
      gradientStops: [1, 0.4, 0],
    },
    movieBarChart: {
      extraOptions: chartConfigs.barChartOptions,
      chartData: {
        labels: ["Comedy", "Biography"],
        datasets: [
          {
            label: "No. of Users",
            fill: true,
            borderColor: "rgb(255, 0, 128)",
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            data: [12, 4],
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
            localStorage.setItem("roomUsers", JSON.stringify(roomUsers));
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
      axios
        .get("/dashboard/" + this.roomCode)
        .then((response) => {
          this.youtubeTop = response.data.youtube;
          this.bookTop = response.data.book;
          this.movieTop = response.data.movie;
          this.spotifyTop = response.data.spotify;
        })
        .catch(() => {
          this.navigateRoute("/questionnaire");
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