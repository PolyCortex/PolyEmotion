namespace MusicPlayerGUI
{
    partial class MainView
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
            this.playlistControl1 = new MusicPlayerGUI.PlaylistControl();
            this.SuspendLayout();
            // 
            // playlistControl1
            // 
            this.playlistControl1.Location = new System.Drawing.Point(24, 11);
            this.playlistControl1.Margin = new System.Windows.Forms.Padding(2);
            this.playlistControl1.Name = "playlistControl1";
            this.playlistControl1.Size = new System.Drawing.Size(700, 563);
            this.playlistControl1.TabIndex = 0;
            // 
            // MainView
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None;
            this.ClientSize = new System.Drawing.Size(854, 585);
            this.Controls.Add(this.playlistControl1);
            this.Name = "MainView";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "MusicPlayerMainView";
            this.ResumeLayout(false);

        }

        #endregion

        private PlaylistControl playlistControl1;
    }
}