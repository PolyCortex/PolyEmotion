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
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.playlistControl1 = new MusicPlayerGUI.PlaylistControl();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.ImageScalingSize = new System.Drawing.Size(32, 32);
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(1452, 24);
            this.menuStrip1.TabIndex = 10;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // playlistControl1
            // 
            this.playlistControl1.Location = new System.Drawing.Point(100, 104);
            this.playlistControl1.Name = "playlistControl1";
            this.playlistControl1.Size = new System.Drawing.Size(881, 383);
            this.playlistControl1.TabIndex = 11;
            // 
            // MainView
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None;
            this.ClientSize = new System.Drawing.Size(1452, 845);
            this.Controls.Add(this.playlistControl1);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "MainView";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "MusicPlayerMainView";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.MenuStrip menuStrip1;
        private PlaylistControl playlistControl1;
    }
}