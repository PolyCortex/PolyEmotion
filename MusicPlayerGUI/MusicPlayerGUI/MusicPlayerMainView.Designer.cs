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
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea1 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend1 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series1 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.axWindowsMediaPlayer1 = new AxWMPLib.AxWindowsMediaPlayer();
            this.songPlaylist = new System.Windows.Forms.ListBox();
            this.labelPlaylist = new System.Windows.Forms.Label();
            this.btnUpdatePlaylist = new System.Windows.Forms.Button();
            this.chart1 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            ((System.ComponentModel.ISupportInitialize)(this.axWindowsMediaPlayer1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).BeginInit();
            this.SuspendLayout();
            // 
            // axWindowsMediaPlayer1
            // 
            this.axWindowsMediaPlayer1.Enabled = true;
            this.axWindowsMediaPlayer1.Location = new System.Drawing.Point(-107, 134);
            this.axWindowsMediaPlayer1.Margin = new System.Windows.Forms.Padding(2);
            this.axWindowsMediaPlayer1.Name = "axWindowsMediaPlayer1";
            this.axWindowsMediaPlayer1.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axWindowsMediaPlayer1.OcxState")));
            this.axWindowsMediaPlayer1.Size = new System.Drawing.Size(570, 340);
            this.axWindowsMediaPlayer1.TabIndex = 0;
            // 
            // songPlaylist
            // 
            this.songPlaylist.FormattingEnabled = true;
            this.songPlaylist.Items.AddRange(new object[] {
            "element 1",
            "element 2",
            "element 3",
            "element 4"});
            this.songPlaylist.Location = new System.Drawing.Point(583, 243);
            this.songPlaylist.Margin = new System.Windows.Forms.Padding(2);
            this.songPlaylist.Name = "songPlaylist";
            this.songPlaylist.ScrollAlwaysVisible = true;
            this.songPlaylist.Size = new System.Drawing.Size(186, 160);
            this.songPlaylist.TabIndex = 6;
            // 
            // labelPlaylist
            // 
            this.labelPlaylist.AutoSize = true;
            this.labelPlaylist.Location = new System.Drawing.Point(660, 134);
            this.labelPlaylist.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelPlaylist.Name = "labelPlaylist";
            this.labelPlaylist.Size = new System.Drawing.Size(39, 13);
            this.labelPlaylist.TabIndex = 8;
            this.labelPlaylist.Text = "Playlist";
            // 
            // btnUpdatePlaylist
            // 
            this.btnUpdatePlaylist.BackColor = System.Drawing.SystemColors.ControlLight;
            this.btnUpdatePlaylist.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnUpdatePlaylist.FlatAppearance.BorderColor = System.Drawing.Color.Black;
            this.btnUpdatePlaylist.FlatAppearance.BorderSize = 2;
            this.btnUpdatePlaylist.FlatAppearance.MouseOverBackColor = System.Drawing.Color.DarkGray;
            this.btnUpdatePlaylist.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnUpdatePlaylist.ForeColor = System.Drawing.SystemColors.WindowText;
            this.btnUpdatePlaylist.Location = new System.Drawing.Point(609, 425);
            this.btnUpdatePlaylist.Margin = new System.Windows.Forms.Padding(2);
            this.btnUpdatePlaylist.Name = "btnUpdatePlaylist";
            this.btnUpdatePlaylist.Size = new System.Drawing.Size(115, 40);
            this.btnUpdatePlaylist.TabIndex = 9;
            this.btnUpdatePlaylist.Text = "Update Playlist";
            this.btnUpdatePlaylist.UseVisualStyleBackColor = false;
            this.btnUpdatePlaylist.Click += new System.EventHandler(this.btnUpdatePlaylist_Click);
            // 
            // chart1
            // 
            chartArea1.Name = "ChartArea1";
            this.chart1.ChartAreas.Add(chartArea1);
            legend1.Name = "Legend1";
            this.chart1.Legends.Add(legend1);
            this.chart1.Location = new System.Drawing.Point(9, 5);
            this.chart1.Margin = new System.Windows.Forms.Padding(2);
            this.chart1.Name = "chart1";
            series1.ChartArea = "ChartArea1";
            series1.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            series1.Legend = "Legend1";
            series1.Name = "Series1";
            this.chart1.Series.Add(series1);
            this.chart1.Size = new System.Drawing.Size(378, 180);
            this.chart1.TabIndex = 10;
            this.chart1.Text = "chart1";
            // 
            // MusicPlayerMainView
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ControlDark;
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None;
            this.ClientSize = new System.Drawing.Size(766, 529);
            this.Controls.Add(this.chart1);
            this.Controls.Add(this.btnUpdatePlaylist);
            this.Controls.Add(this.labelPlaylist);
            this.Controls.Add(this.songPlaylist);
            this.Controls.Add(this.axWindowsMediaPlayer1);
            this.Cursor = System.Windows.Forms.Cursors.Arrow;
            this.Margin = new System.Windows.Forms.Padding(2);
            this.Name = "MusicPlayerMainView";
            this.Text = "MusicPlayerMainView";
            ((System.ComponentModel.ISupportInitialize)(this.axWindowsMediaPlayer1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private AxWMPLib.AxWindowsMediaPlayer axWindowsMediaPlayer1;
        private System.Windows.Forms.ListBox songPlaylist;
        private System.Windows.Forms.Label labelPlaylist;
        private System.Windows.Forms.Button btnUpdatePlaylist;
        private System.Windows.Forms.DataVisualization.Charting.Chart chart1;
    }
}