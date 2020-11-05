
import { Pie, mixins } from 'vue-chartjs'

export default {
    name: "pie-chart",
    extends: Pie,
    mixins: [mixins.reactiveProp],
    // props: ['options'],
    data () {
        return {
            ctx: null,
        // return {
        // chartData: {
        //     labels: ["Italy", "India", "Japan", "USA",],
        //     datasets: [{
        //         borderWidth: 1,
        //         borderColor: [
        //         'rgba(255,99,132,1)',
        //         'rgba(54, 162, 235, 1)',
        //         'rgba(255, 206, 86, 1)',
        //         'rgba(75, 192, 192, 1)'            
        //         ],
        //         backgroundColor: [
        //         'rgba(255, 99, 132, 0.8)',
        //         'rgba(54, 162, 235, 0.8)',
        //         'rgba(255, 206, 86, 0.8)',
        //         'rgba(75, 192, 192, 0.8)',                
        //         ],
        //         data: [1000,	500,	1500,	1000]
        //     }]
        // },
            options: {
                legend: {
                    display: true,
                    labels: {
                        fontColor: 'white'
                    }
                },
                responsive: true,
                maintainAspectRatio: false
            }
        }
    },
    // Figure out how to update the data, dk is it sth to do with the method in BarChart?
    mounted () {
        this.renderChart(this.chartData, this.options)
    }
    // mounted() {
    //     this.$watch('chartData', (newVal, oldVal) => {
    //       this.updateGradients(newVal);
    //       if (!oldVal) {
    //         this.renderChart(
    //           this.chartData,
    //           this.extraOptions
    //         );
    //       }
    //     }, { immediate: true });
    //   }
}