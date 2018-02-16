using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using LiveCharts;
using LiveCharts.Wpf;
using LiveCharts.WinForms;
using LiveCharts.Configurations;

static class Constants
{
    public const int REFRESH_RATE = 50;
}

namespace MusicPlayerGUI {
    public partial class GraphControl : UserControl
    {
        public ChartValues<DataModel> values { get; set; }
        public ChartValues<DataModel> values2 { get; set; }
        public Timer timer { get; set; }
        public Random randomGenerator { get; set; }
        public GraphControl() {
            InitializeComponent();
            //graphSignal1.AnimationsSpeed = System.TimeSpan.FromMilliseconds(Constants.REFRESH_RATE);
            graphSignal1.DisableAnimations = true;

            // We define our axis on the DataModel.
            var mapper = Mappers.Xy<DataModel>()
                .X(model => model.mockTimeStamp.Ticks)
                .Y(model => model.value);
            Charting.For<DataModel>(mapper);

            values = new ChartValues<DataModel>();
            values2 = new ChartValues<DataModel>();
            graphSignal1.Series = new SeriesCollection
            {
                new LineSeries {    // We define a new line serie for our graph
                    Values = values,
                    PointGeometrySize = 3,
                    StrokeThickness = 1
                },
                new LineSeries {    // We define a new line serie for our graph
                    Values = values2,
                    PointGeometrySize = 3,
                    StrokeThickness = 1
                }
            };
            graphSignal1.AxisX.Add(new Axis {
                DisableAnimations = false,
                LabelFormatter = value => new System.DateTime((long)value).ToString("mm:ss"),
                Separator = new Separator {
                    Step = TimeSpan.FromSeconds(1).Ticks
                }
            });

            SetAxisLimits(System.DateTime.Now);

            //The next code simulates data changes every 50 ms
            timer = new Timer {
                Interval = Constants.REFRESH_RATE
            };
            timer.Tick += TimerOnTick;
            randomGenerator = new Random();
            timer.Start();
        }
        private void SetAxisLimits(System.DateTime now) {
            // graphSignal1.AxisX[0].MaxValue = now.Ticks + TimeSpan.FromSeconds(0).Ticks; // force the axis to be 0 seconds ahead
            graphSignal1.AxisX[0].MinValue = now.Ticks - TimeSpan.FromSeconds(10).Ticks; // 10 seconds are shown on the axis
        }
        private void TimerOnTick(object sender, EventArgs eventArgs) {
            var now = System.DateTime.Now;
            values.Add(new DataModel
            {
                mockTimeStamp = now,
                value = randomGenerator.Next(0, 30)
            });

            values2.Add(new DataModel
            {
                mockTimeStamp = now,
                value = randomGenerator.Next(0, 10)
            });

            SetAxisLimits(now);
            //lets only use the last 30 values
            if (values.Count > 120)
                values.RemoveAt(0);
            if (values2.Count > 120)
                values2.RemoveAt(0);
        }
    }
}
