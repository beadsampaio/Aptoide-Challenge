package com.android.support.exercise.ui

import android.os.Bundle
import android.widget.ImageView
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.android.support.exercise.R
import com.android.support.exercise.bd.AppDatabase
import com.android.support.exercise.ui.adapters.PostAdapter
import com.android.support.exercise.ui.viewmodel.MainActivityViewModel
import com.bumptech.glide.Glide

class MainActivity : AppCompatActivity() {

    private val viewModel = MainActivityViewModel()

    private lateinit var postAdapter: PostAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        setContentView(R.layout.activity_main)

        //AppDatabase.initDatabase(applicationContext)

        val textView = findViewById<TextView>(R.id.text_view_user)
        viewModel.userName.observeForever {
            textView.text = it
        }

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        val imageView = findViewById<ImageView>(R.id.image_view_user)

        viewModel.userImage.observeForever {
            Glide.with(this@MainActivity).load(it).into(imageView)
        }

        val recyclerView = findViewById<RecyclerView>(R.id.recycler_view_posts)
        recyclerView.layoutManager = LinearLayoutManager(this)

        postAdapter = PostAdapter()
        recyclerView.adapter = postAdapter

        viewModel.posts.observeForever {
            postAdapter.setPosts(it)
        }

        viewModel.loadPostsData()
        viewModel.loadUserData(applicationContext)
    }
}