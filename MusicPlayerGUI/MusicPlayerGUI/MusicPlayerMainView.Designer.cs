namespace MusicPlayerGUI
{
    partial class MusicPlayerMainView
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MusicPlayerMainView));
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea6 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend6 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series6 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.mediaPlayer = new AxWMPLib.AxWindowsMediaPlayer();
            this.songPlaylist = new System.Windows.Forms.ListBox();
            this.labelPlaylist = new System.Windows.Forms.Label();
            this.btnUpdatePlaylist = new System.Windows.Forms.Button();
            this.chart1 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            ((System.ComponentModel.ISupportInitialize)(this.mediaPlayer)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).BeginInit();
            this.SuspendLayout();
            // 
            // mediaPlayer
            // 
            this.mediaPlayer.Enabled = true;
            this.mediaPlayer.Location = new System.Drawing.Point(12, 299);
            this.mediaPlayer.Name = "mediaPlayer";
            this.mediaPlayer.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("mediaPlayer.OcxState")));
            this.mediaPlayer.Size = new System.Drawing.Size(570, 340);
            this.mediaPlayer.TabIndex = 0;
            // 
            // songPlaylist
            // 
            this.songPlaylist.FormattingEnabled = true;
            this.songPlaylist.HorizontalScrollbar = true;
            this.songPlaylist.ItemHeight = 16;
            this.songPlaylist.Location = new System.Drawing.Point(588, 324);
            this.songPlaylist.Name = "songPlaylist";
            this.songPlaylist.ScrollAlwaysVisible = true;
            this.songPlaylist.Size = new System.Drawing.Size(247, 260);
            this.songPlaylist.TabIndex = 6;
            this.songPlaylist.SelectedIndexChanged += new System.EventHandler(this.songPlaylist_SelectedIndexChanged);
            // 
            // labelPlaylist
            // 
            this.labelPlaylist.AutoSize = true;
            this.labelPlaylist.Location = new System.Drawing.Point(664, 299);
            this.labelPlaylist.Name = "labelPlaylist";
            this.labelPlaylist.Size = new System.Drawing.Size(52, 17);
            this.labelPlaylist.TabIndex = 8;
            this.labelPlaylist.Text = "Playlist";
            // 
            // btnUpdatePlaylist
            // 
            this.btnUpdatePlaylist.Location = new System.Drawing.Point(588, 590);
            this.btnUpdatePlaylist.Name = "btnUpdatePlaylist";
            this.btnUpdatePlaylist.Size = new System.Drawing.Size(153, 49);
            this.btnUpdatePlaylist.TabIndex = 9;
            this.btnUpdatePlaylist.Text = "Update Playlist";
            this.btnUpdatePlaylist.UseVisualStyleBackColor = true;
            this.btnUpdatePlaylist.Click += new System.EventHandler(this.btnUpdatePlaylist_Click);
            // 
            // chart1
            // 
            chartArea6.Name = "ChartArea1";
            this.chart1.ChartAreas.Add(chartArea6);
            legend6.Name = "Legend1";
            this.chart1.Legends.Add(legend6);
            this.chart1.Location = new System.Drawing.Point(12, 30);
            this.chart1.Name = "chart1";
            series6.ChartArea = "ChartArea1";
            series6.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            series6.Legend = "Legend1";
            series6.Name = "Series1";
            this.chart1.Series.Add(series6);
            this.chart1.Size = new System.Drawing.Size(504, 221);
            this.chart1.TabIndex = 10;
            this.chart1.Text = "chart1";
            // 
            // MusicPlayerMainView
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None;
            this.ClientSize = new System.Drawing.Size(1011, 690);
            this.Controls.Add(this.chart1);
            this.Controls.Add(this.btnUpdatePlaylist);
            this.Controls.Add(this.labelPlaylist);
            this.Controls.Add(this.songPlaylist);
            this.Controls.Add(this.mediaPlayer);
            this.Name = "MusicPlayerMainView";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "MusicPlayerMainView";
            this.Load += new System.EventHandler(this.MusicPlayerMainView_Load);
            ((System.ComponentModel.ISupportInitialize)(this.mediaPlayer)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private AxWMPLib.AxWindowsMediaPlayer mediaPlayer;
        private System.Windows.Forms.ListBox songPlaylist;
        private System.Windows.Forms.Label labelPlaylist;
        private System.Windows.Forms.Button btnUpdatePlaylist;
        private System.Windows.Forms.DataVisualization.Charting.Chart chart1;
    }
}