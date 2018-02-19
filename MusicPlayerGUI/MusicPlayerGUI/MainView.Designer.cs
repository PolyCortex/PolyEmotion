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
            this.tabControlMainView = new System.Windows.Forms.TabControl();
            this.tabPageFreeMode = new System.Windows.Forms.TabPage();
            this.tabPageEmotionMode = new System.Windows.Forms.TabPage();
            this.playlistControl1 = new MusicPlayerGUI.PlaylistControl();
            this.tabControlMainView.SuspendLayout();
            this.tabPageFreeMode.SuspendLayout();
            this.SuspendLayout();
            // 
            // tabControlMainView
            // 
            this.tabControlMainView.Alignment = System.Windows.Forms.TabAlignment.Left;
            this.tabControlMainView.Controls.Add(this.tabPageFreeMode);
            this.tabControlMainView.Controls.Add(this.tabPageEmotionMode);
            this.tabControlMainView.DrawMode = System.Windows.Forms.TabDrawMode.OwnerDrawFixed;
            this.tabControlMainView.ItemSize = new System.Drawing.Size(25, 100);
            this.tabControlMainView.Location = new System.Drawing.Point(-4, 0);
            this.tabControlMainView.Multiline = true;
            this.tabControlMainView.Name = "tabControlMainView";
            this.tabControlMainView.SelectedIndex = 0;
            this.tabControlMainView.Size = new System.Drawing.Size(1181, 733);
            this.tabControlMainView.TabIndex = 0;
            this.tabControlMainView.DrawItem += new System.Windows.Forms.DrawItemEventHandler(this.tabControlMainView_DrawItem);
            // 
            // tabPageFreeMode
            // 
            this.tabPageFreeMode.Controls.Add(this.playlistControl1);
            this.tabPageFreeMode.Location = new System.Drawing.Point(104, 4);
            this.tabPageFreeMode.Name = "tabPageFreeMode";
            this.tabPageFreeMode.Padding = new System.Windows.Forms.Padding(3);
            this.tabPageFreeMode.Size = new System.Drawing.Size(1073, 725);
            this.tabPageFreeMode.TabIndex = 0;
            this.tabPageFreeMode.Text = "Free Mode";
            this.tabPageFreeMode.UseVisualStyleBackColor = true;
            // 
            // tabPageEmotionMode
            // 
            this.tabPageEmotionMode.Location = new System.Drawing.Point(104, 4);
            this.tabPageEmotionMode.Name = "tabPageEmotionMode";
            this.tabPageEmotionMode.Padding = new System.Windows.Forms.Padding(3);
            this.tabPageEmotionMode.Size = new System.Drawing.Size(1073, 725);
            this.tabPageEmotionMode.TabIndex = 1;
            this.tabPageEmotionMode.Text = "Emotion Mode";
            this.tabPageEmotionMode.UseVisualStyleBackColor = true;
            // 
            // playlistControl1
            // 
            this.playlistControl1.Location = new System.Drawing.Point(5, 5);
            this.playlistControl1.Margin = new System.Windows.Forms.Padding(2);
            this.playlistControl1.Name = "playlistControl1";
            this.playlistControl1.Size = new System.Drawing.Size(907, 520);
            this.playlistControl1.TabIndex = 0;
            // 
            // MainView
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None;
            this.ClientSize = new System.Drawing.Size(1176, 734);
            this.Controls.Add(this.tabControlMainView);
            this.Name = "MainView";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "MusicPlayerMainView";
            this.tabControlMainView.ResumeLayout(false);
            this.tabPageFreeMode.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TabControl tabControlMainView;
        private System.Windows.Forms.TabPage tabPageFreeMode;
        private System.Windows.Forms.TabPage tabPageEmotionMode;
        private PlaylistControl playlistControl1;
    }
}